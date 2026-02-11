import streamlit as st
import pandas as pd
from utils.db_utils import get_engine, get_schema_preview, run_query
from utils.llm_utils import get_sql_query_from_nl
from utils.auth_utils import admin_login
from sqlalchemy import inspect

# Streamlit page setup
st.set_page_config(page_title="Enhanced SQL Chatbot", layout="wide", initial_sidebar_state="expanded")

# App header
st.title("🤖 Enhanced SQL Chatbot (MySQL and POSTGRES Edition)")
st.caption("Chat with your MySQL database using Groq + LangChain")

# 🌙 Dark theme
st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="stAppViewContainer"] {
    background-color: #0E1117;
    color: #FAFAFA;
}
[data-testid="stSidebar"] * {
    color: #FAFAFA !important;
}
</style>
""", unsafe_allow_html=True)

# 🔐 Admin login
admin_login()
is_admin = st.session_state.get("is_admin", False)

# 🛠 Database connection sidebar
st.sidebar.header("⚙️ Database Configuration")
db_type = st.sidebar.selectbox("Database Type", ["mysql", "postgres", "sqlite"])

if db_type == "sqlite":
    database = "local.db"
    user = password = host = None
    port = None
else:
    if db_type == "mysql":
        user = st.sidebar.text_input("MySQL User", value="root")
        port = None
    else:  # postgres
        user = st.sidebar.text_input("PostgreSQL User", value="postgres")
        port = st.sidebar.number_input("Port", value=5432, min_value=1, max_value=65535)
    
    password = st.sidebar.text_input("Password", type="password")
    host = st.sidebar.text_input("Host", value="localhost")
    database = st.sidebar.text_input("Database", value="test")

if st.sidebar.button("Connect"):
    try:
        if db_type == "postgres":
            engine = get_engine(db_type, user, password, host, database, port)
        else:
            engine = get_engine(db_type, user, password, host, database)
        schema = get_schema_preview(engine)
        st.session_state.engine = engine
        st.session_state.schema = schema
        st.session_state.chat_history = []
        st.sidebar.success("✅ Connected successfully!")
    except Exception as e:
        st.sidebar.error(f"Connection failed: {e}")

# Admin-controlled write toggle (enable UPDATE/DELETE)
if is_admin:
    write_enable = st.sidebar.checkbox("Enable write operations (UPDATE/DELETE)", value=st.session_state.get("allow_write", False))
    st.session_state.allow_write = write_enable
else:
    # ensure write is off for non-admins
    st.session_state.allow_write = False
    st.sidebar.info("Write operations disabled. Login as admin to enable.")

# 🗂 Schema explorer
if "engine" in st.session_state:
    st.sidebar.header("🗂 Schema Explorer")
    inspector = inspect(st.session_state.engine)
    tables = inspector.get_table_names()

    for table in tables:
        with st.sidebar.expander(f"📋 {table}"):
            cols = inspector.get_columns(table)
            col_info = "\n".join([f"- {c['name']} ({c['type']})" for c in cols])
            st.sidebar.markdown(col_info)

            if st.sidebar.button(f"👁 View Sample - {table}", key=f"view-{table}"):
                df = run_query(st.session_state.engine, f"SELECT * FROM {table} LIMIT 5;")
                if isinstance(df, str):
                    st.sidebar.error(df)
                else:
                    st.sidebar.dataframe(df)

# 💬 Chat interface
if "engine" in st.session_state:
    st.subheader("💬 Ask Your Database")

    # Display chat history
    for msg in st.session_state.get("chat_history", []):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Get user question
    if prompt := st.chat_input("Type your question..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # 🧠 Step 1: Convert question → SQL
        with st.spinner("🧠 Translating to SQL..."):
            sql = get_sql_query_from_nl(prompt, st.session_state.schema)

        # 🧹 Clean SQL (remove markdown fences or extra text)
        if sql:
            sql = sql.strip().replace("```sql", "").replace("```", "").strip()

        # 💬 Display SQL
        st.chat_message("assistant").markdown(f"**SQL Generated:**\n```sql\n{sql}\n```")

        # 🚀 Step 2: Execute SQL query
        with st.spinner("🚀 Executing query..."):
            result = run_query(st.session_state.engine, sql, allow_write=st.session_state.get("allow_write", False))

        # ✅ Step 3: Show results or errors
        if isinstance(result, str) and "Error" in result:
            st.error(result)
        elif isinstance(result, pd.DataFrame) and not result.empty:
            st.dataframe(result.head())
            csv = result.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download CSV", csv, "result.csv", "text/csv")
        elif isinstance(result, pd.DataFrame) and result.empty:
            st.warning("⚠️ No results found for this query.")
        else:
            st.empty()  # prevents 'undefined' output
