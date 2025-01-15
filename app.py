import streamlit as st
from time import sleep
from login import login_page
from register import register_page
from dashboard import dashboard_page
from income import income_page
from welcome import welcome_page
from profilePage import profile_page
from category import category_page
from expense import expense_page
from viewSummary import viewSummary_page
from view_income import view_income_page

# Load CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the external CSS
load_css("Css/style.css")  # Adjust the path if needed

def main():
    # Initialize session state for navigation
    if "page" not in st.session_state:
        st.session_state["page"] = "Login"

    # Define all pages
    pages = {
        "Dashboard": dashboard_page,
        "Login": login_page,
        "Register": register_page,
        "Income": income_page,
        "Welcome": welcome_page,
        "ProfilePage": profile_page,
        "Category": category_page,  # Add category_page to the dictionary
        "expense": expense_page,
        "viewSummary": viewSummary_page,
        "view_income": view_income_page
    }
    # Sidebar Navigation
    st.sidebar.title("🔅〽️ Navigation")
    
    if "user" not in st.session_state:  # If user is not logged in
        st.session_state["page"] = st.sidebar.radio("Go to", ["Login"])
    else:  # If user is logged in
        role = st.session_state["user"]["role"]
        if role == "user": 
            st.session_state["page"] = st.sidebar.radio("Go to", ["Welcome", "Income", "expense", "Category", "viewSummary","view_income", "ProfilePage", "Logout"])
        elif role == "admin":
            st.session_state["page"] = st.sidebar.radio("Go to", ["Dashboard", "Register", "ProfilePage", "Logout"])

    # Handle Logout
    if st.session_state["page"] == "Logout":   
        st.session_state.clear()         
        st.session_state["page"] = "Login"       
        sleep(0.5)
        st.switch_page("./app.py")

    else:
        # Render the selected page
        if st.session_state["page"] in pages:
            pages[st.session_state["page"]]()
        else:
            st.error("Page not found!")

        hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>   
                    """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

   

if __name__ == "__main__":
    main()
