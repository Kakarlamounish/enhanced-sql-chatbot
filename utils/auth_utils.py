import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

def admin_login():
    st.sidebar.subheader("🔐 Admin Login")

    # Initialize session state for admin if not present
    if "is_admin" not in st.session_state:
        st.session_state.is_admin = False

    # If already logged in, show status and provide logout
    if st.session_state.is_admin:
        st.sidebar.markdown(f"**Logged in as:** {os.getenv('ADMIN_USER')}")
        if st.sidebar.button("Logout"):
            st.session_state.is_admin = False
            st.sidebar.info("Logged out.")
        return True

    # Not logged in: show login fields
    user = st.sidebar.text_input("Admin Username")
    password = st.sidebar.text_input("Admin Password", type="password")

    if st.sidebar.button("Login"):
        if user == os.getenv("ADMIN_USER") and password == os.getenv("ADMIN_PASSWORD"):
            st.session_state.is_admin = True
            st.sidebar.success("✅ Admin authenticated!")
            return True
        else:
            st.sidebar.error("❌ Invalid credentials.")
    return False
