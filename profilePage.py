import streamlit as st
from time import sleep

def profile_page():

   if "user" in st.session_state:
      user = st.session_state["user"]
      st.subheader("🔅〽️ User Profile")

      st.write(f"User Name is : {user['username']}👤")
      st.write(f"Yourn Role is : {user['role']}🔐")

   # if st.button("Logout", type="primary"):
   #     st.session_state.clear()  # Clear all session state
   #     sleep(0.5)  # Optional delay for UX
   #     st.session_state["page"] = "Login"  # Redirect to login page
   #     st.experimental_rerun()  # Reload the app
   # else:
   #     st.warning("⚠️ Please log in to view this page.")