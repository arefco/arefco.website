import streamlit as st
from db_utils import fetch_summary
import pandas as pd
from datetime import date


def viewSummary_page():
    if "user" in st.session_state:
        user = st.session_state["user"]
        user_id = user["user_id"]  # Get the user_id from the session state
        st.subheader(f"🔅〽️ MONTHLY FINANCES (ميزانتي الشهرية)")

        # Select month and year
        today = date.today()
        selected_month = st.selectbox(
            ":orange[Select Month]", range(1, 13), format_func=lambda x: date(1900, x, 1).strftime("%B")
        )
        selected_year = st.number_input(
            ":orange[Select Year]", min_value=2000, max_value=today.year, value=today.year, step=1
        )
    if st.button("Show"):
        try:
            total_income, total_expenses, detailed_expenses = fetch_summary(user_id, selected_month, selected_year)

            st.write(f":orange[MY CASHFLOW]  [{date(1900, selected_month, 1).strftime('%B')} , {selected_year}]")
            
            # Summary table
            summary_data = {
                "Description": ["Total Income (الدخل)", "Total Expenses (نفقات)", "Net Savings (الادخار)"],
                "Amount (AED)": [
                    f"{total_income:,.0f}",
                    f"{total_expenses:,.0f}",
                    f"{total_income - total_expenses:,.0f}",
                ],
            }
            summary_df = pd.DataFrame(summary_data)
            st.table(summary_df)

            # Breakdown of net savings
            net_savings = total_income - total_expenses
            if net_savings > 0:
                st.write(":orange[MY SAVING (مدخراتي)]" )
                savings_breakdown = {
                    "First Saving (التوفير الاول) (25%)": 0.25 * net_savings,
                    "Emergency Fund (صندوق الطوارئ) (30%)": 0.30 * net_savings,
                    "Debt Plan (خطة الديون) (20%)": 0.20 * net_savings,
                    "Second Saving (التوفيرالثاني)/(25%)": 0.25 * net_savings,
                }
                breakdown_data = {
                    "Category": savings_breakdown.keys(),
                    "Amount (AED)": [f"{amount:,.0f}" for amount in savings_breakdown.values()],
                }
                breakdown_df = pd.DataFrame(breakdown_data)
                st.table(breakdown_df)
            else:
                st.info("No savings available to calculate percentages.")

            # Detailed expenses table
            if detailed_expenses:
                st.write(":green[MY EXPENSES (مصاريفي) ]")
                expense_data = {
                    "Amount (AED)": [f"{row['amount']:,.0f}" for row in detailed_expenses],
                    "Category": [row['category'] for row in detailed_expenses],
                    "Transaction Date": [row['transaction_date'].strftime("%Y-%m-%d") for row in detailed_expenses],
                }
                expense_df = pd.DataFrame(expense_data)
                st.table(expense_df)
            else:
                st.write("No expenses found for this month and year.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")




