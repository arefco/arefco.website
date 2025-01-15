#new code to improve login users

import streamlit as st
from db_utils import authenticate_user
from time import sleep

# Custom CSS to adjust input field size
st.markdown("""
    <style>
    .input-field {
        font-size: 16px; /* Adjust text size inside input */
        width: 30px; /* Adjust width */
        height: 40px; /* Adjust height */
        padding: 5px; /* Add padding */
    }
    </style>
""", unsafe_allow_html=True)

def login_page():
    st.subheader("〽️ Login")
    username = st.text_input("👤 User Name", key="username", placeholder="Enter your username here")
    password = st.text_input("🔐 Password", type="password", key="password", placeholder="********")

    if st.button("Login", type="primary"):
        user = authenticate_user(username, password)  # Assuming authenticate_user returns a tuple (user_id, username, role)
        if user:
            # Store user data in session state
            st.session_state["user"] = {"user_id": user[0], "username": user[1], "role": user[2]}
            st.success(f"Logged in as {user[1]} ({user[2]})")
            st.session_state["page"] = "welcome" if user[2] == "user" else "dashboard"
            sleep(0.5)
            st.switch_page("app.py")
           # st.experimental_rerun()  # This reloads the app to show the correct page
        else:
            st.error("〽️ Invalid username or password")




#working code 
# import streamlit as st
# from db_utils import authenticate_user
# from time import sleep


# # Custom CSS to adjust input field size
# st.markdown("""
#     <style>
#     .input-field {
#         font-size: 16px; /* Adjust text size inside input */
#         width: 30px; /* Adjust width */
#         height: 40px; /* Adjust height */
#         padding: 5px; /* Add padding */
#     }
#     </style>
# """, unsafe_allow_html=True)

# def login_page():
#     st.subheader("〽️Login")
#     username = st.text_input("👤 User Name", key="username", placeholder="Enter your username here")
#     password = st.text_input("🔐 Password", type="password", key="password", placeholder="********")

    
#     if st.button("Login",  type="primary"):
#         user = authenticate_user(username, password)
#         if user:
#             st.session_state["user"] = {"user": user[0], "username": user[1], "role": user[2]}
#             st.success(f"Logged in as {user[1]} ({user[2]})")
#             st.session_state["page"] = "welcome" if user[2] == "user" else "dashboard"
#             sleep(0.5)
#             st.switch_page("app.py")
#         else:
#                 st.error("〽️ Invalid username or password")

