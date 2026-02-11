from sqlalchemy import create_engine, text
import pandas as pd
import re

def get_engine(db_type, user=None, password=None, host=None, database=None, port=None):
    """Create SQLAlchemy engine for MySQL, PostgreSQL, or SQLite"""
    if db_type == "mysql":
        url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
    elif db_type == "postgres":
        port = port or 5432
        url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    elif db_type == "sqlite":
        url = "sqlite:///local.db"
    else:
        raise ValueError("Unsupported database type. Use 'mysql', 'postgres', or 'sqlite'.")
    return create_engine(url)


def run_query(engine, query, allow_write: bool = False):
    """Execute SQL query safely and return results as DataFrame.

    Security rules:
    - `DROP`, `TRUNCATE`, and `ALTER` are always blocked.
    - `UPDATE` and `DELETE` are blocked unless `allow_write=True`.
    """
    try:
        # --- Clean up LLM-style Markdown formatting ---
        query = query.strip()
        if query.startswith("```sql"):
            query = query.replace("```sql", "").replace("```", "").strip()
        elif query.startswith("```"):
            query = query.replace("```", "").strip()

        q_up = query.upper()

        # --- Dialect-aware normalization: convert active = 0/1 to TRUE/FALSE for Postgres ---
        try:
            dialect_name = getattr(engine, "dialect").name or ""
        except Exception:
            dialect_name = ""
        if "postgres" in dialect_name.lower():
            # replace active assignments (case-insensitive)
            query = re.sub(r"(?i)\bactive\s*=\s*0\b", "active = FALSE", query)
            query = re.sub(r"(?i)\bactive\s*=\s*1\b", "active = TRUE", query)
            q_up = query.upper()

        # --- Always-blocked operations ---
        forbidden_always = ["DROP", "TRUNCATE", "ALTER"]
        if any(word in q_up for word in forbidden_always):
            return f"⚠️ Dangerous query blocked for safety: {query}"

        # --- Handle DELETE -> soft-delete conversion (admin-enabled) ---
        if "DELETE" in q_up:
            if not allow_write:
                return f"⚠️ Write operations (UPDATE/DELETE) are disabled. Enable write mode as an admin to run this query."
            # Try to convert DELETE FROM <table> WHERE ...  -> UPDATE <table> SET active = 0 WHERE ...
            # Require a WHERE clause to avoid mass-updates
            m = re.match(r"\s*DELETE\s+FROM\s+[`\"]?([\w]+)[`\"]?\s*(WHERE\s+.+)", query, flags=re.IGNORECASE)
            if m:
                table = m.group(1)
                where_clause = m.group(2)
                # build soft-delete UPDATE with dialect-aware boolean
                dialect_name = ""
                try:
                    dialect_name = getattr(engine, "dialect").name or ""
                except Exception:
                    dialect_name = ""
                if "postgres" in dialect_name.lower():
                    active_literal = "FALSE"
                else:
                    # MySQL/SQLite use 0/1 for booleans
                    active_literal = "0"
                query = f"UPDATE {table} SET active = {active_literal} {where_clause}"
                q_up = query.upper()
            else:
                return "⚠️ Unsafe DELETE detected. Please include a WHERE clause (e.g. DELETE FROM table WHERE id = ...)."

        # --- Write operations: allowed only when explicitly enabled ---
        forbidden_write = ["DELETE", "UPDATE"]
        if any(word in q_up for word in forbidden_write) and not allow_write:
            return f"⚠️ Write operations (UPDATE/DELETE) are disabled. Enable write mode as an admin to run this query."

        # --- Execute query ---
        with engine.connect() as conn:
            # Read queries -> return DataFrame
            if q_up.startswith("SELECT") or q_up.startswith("WITH") or q_up.startswith("SHOW") or q_up.startswith("PRAGMA"):
                result = pd.read_sql(text(query), conn)
                return result
            # Non-select queries (writes) -> execute and return summary
            else:
                with conn.begin():
                    res = conn.execute(text(query))
                try:
                    rowcount = res.rowcount
                except Exception:
                    rowcount = None
                return f"✅ Query executed successfully. Rows affected: {rowcount}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


def get_schema_preview(engine):
    """Return database tables and their columns"""
    from sqlalchemy import inspect
    inspector = inspect(engine)
    schema = {}
    for table in inspector.get_table_names():
        columns = [col["name"] for col in inspector.get_columns(table)]
        schema[table] = columns
    return schema
