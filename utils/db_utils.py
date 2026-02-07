from sqlalchemy import create_engine, text
import pandas as pd

def get_engine(db_type, user=None, password=None, host=None, database=None):
    """Create SQLAlchemy engine for MySQL or SQLite"""
    if db_type == "mysql":
        url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
    elif db_type == "sqlite":
        url = "sqlite:///local.db"
    else:
        raise ValueError("Unsupported database type.")
    return create_engine(url)


def run_query(engine, query):
    """Execute SQL query safely and return results as DataFrame"""
    try:
        # --- Clean up LLM-style Markdown formatting ---
        query = query.strip()
        if query.startswith("```sql"):
            query = query.replace("```sql", "").replace("```", "").strip()
        elif query.startswith("```"):
            query = query.replace("```", "").strip()

        # --- Optional: prevent dangerous queries (safety check) ---
        forbidden = ["DROP", "DELETE", "TRUNCATE", "ALTER", "UPDATE"]
        if any(word in query.upper() for word in forbidden):
            return f"⚠️ Dangerous query blocked for safety: {query}"

        # --- Execute query ---
        with engine.connect() as conn:
            result = pd.read_sql(text(query), conn)
        return result

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
