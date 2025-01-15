import streamlit as st
from time import sleep
from datetime import date
from db_utils import add_income

def income_page():
    # Check if the user is logged in
    if "user" in st.session_state:
        user = st.session_state["user"]
        user_id = user.get("user_id")  # Get the logged-in user's ID

        st.subheader(f"🔅〽️ Insert Your Income (أدخال دخلك الشهرية)")       
        
        # Input fields for income entry
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        iName = st.text_input("Income Name")
        tdate = st.date_input("Income Date", value=date.today())
        description = st.text_area("Description")

        # Check if the user clicked the "Add" button
        if st.button("Add", type="primary"):
            if amount > 0 and iName.strip():  # Ensure valid input
                try:
                    # Call the add_income function and pass user_id along with other parameters
                    add_income(amount, iName, tdate, description, user_id)  # Include user_id
                    st.success("Income record inserted successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Amount must be greater than 0, and Income Name cannot be empty!")
