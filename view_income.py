import streamlit as st
from db_utils import fetch_user_incomes
import pandas as pd

def view_income_page():
    if "user" in st.session_state:
        user = st.session_state["user"]
        user_id = user["user_id"]  # Getting the user_id from session state
        
        st.subheader(f"🔅〽️ View Income Data (Income of {user['username']})")

        try:
            # Fetch income data for the specific user
            incomes = fetch_user_incomes(user_id)

            if incomes:
                # Create a DataFrame for displaying
                income_data = {
                    "Income Name": [income['iName'] for income in incomes],
                    "Amount (AED)": [f"{income['Amount']:.2f}" for income in incomes],
                    "Income Date": [income['IncomeDate'].strftime("%Y-%m-%d") for income in incomes],
                    "Description": [income['Description'] for income in incomes],
                }

                income_df = pd.DataFrame(income_data)
                st.table(income_df)
            else:
                st.write("No income records found for this user.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")



# import streamlit as st
# from db_utils import fetch_user_income  # This function should already fetch data from your database
# from datetime import date

# def view_income_page():
#     if "user" in st.session_state:
#         user = st.session_state["user"]
#         user_id = user["user_id"]  # Make sure the user_id is stored during login
        
#         st.subheader("🔅〽️ View Your Income")

#         # Fetch the user's income data from the database
#         try:
#             # Filter income records by user_id
#             all_incomes = fetch_user_income()  # Adjust this to filter by user_id
            
#             user_incomes = [income for income in all_incomes if income["user_id"] == user_id]
            
#             if user_incomes:
#                 # Display the income data in a table
#                 st.write(f"Displaying {len(user_incomes)} income records.")
#                 for income in user_incomes:
#                     st.write(f"Amount: {income['amount']} | Name: {income['iName']} | Date: {income['IncomeDate']} | Description: {income['description']}")
#             else:
#                 st.write("No income records found for this user.")
        
#         except Exception as e:
#             st.error(f"Error fetching income data: {e}")

