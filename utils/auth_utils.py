import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

def admin_login():
    st.sidebar.subheader("🔐 Admin Login (MySQL Access)")
    user = st.sidebar.text_input("Admin Username")
    password = st.sidebar.text_input("Admin Password", type="password")

    if st.sidebar.button("Login"):
        if user == os.getenv("MYSQL_USER") and password == os.getenv("MYSQL_PASSWORD"):
            st.sidebar.success("✅ Admin authenticated!")
            return True
        else:
            st.sidebar.error("❌ Invalid credentials.")
    return False
