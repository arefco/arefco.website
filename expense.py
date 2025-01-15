import streamlit as st
from db_utils import insert_expense, fetch_categories
from datetime import date

def expense_page():
    if "user" in st.session_state:
        user = st.session_state["user"]
        user_id = user.get("user_id")  # Fetch user_id from session state
        st.subheader("🔅〽️ Insert New Expense (أخال مصرفاتك الشهرية)")       
 
        # Input fields for expenses
        tdate = st.date_input("Transaction Date", value=date.today())
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")

        # Fetch categories for dropdown
        try:
            categories = fetch_categories()
            if categories:
                category_options = {category["Category_name"]: category["id"] for category in categories}
                selected_category = st.selectbox("Select Category for expense", options=list(category_options.keys()))
                description = st.text_area("Description")
            else:
                st.error("No categories found! Please add categories first.")
                selected_category = None
        except Exception as e:
            st.error(f"Error loading categories: {e}")
            selected_category = None

        # Insert expense record when button is clicked
        if st.button("Insert"):
            if amount > 0:
                try:
                    if selected_category:
                        category_id = category_options[selected_category]
                        tdate = str(tdate)  # Convert date to string if needed for Access
                        
                        # Insert expense into the database, including user_id
                        insert_expense(tdate, float(amount), description.strip(), int(category_id), user_id)
                        st.success("Expense record inserted successfully!")
                    else:
                        st.error("Please select a valid category.")
                except Exception as e:
                    st.error(f"Error inserting record: {e}")
            else:
                st.error("Amount must be greater than 0, and cannot be empty!")
