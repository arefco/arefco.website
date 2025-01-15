import streamlit as st
from db_utils import add_user

def register_page():
    st.subheader("🖋️ Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["user", "admin"])
    
    if st.button("Register", type="primary"):
        result = add_user(username, password, role)
        if result is True:
            st.success("User registered successfully!")
        else:
            st.error(f"Error: {result}")
