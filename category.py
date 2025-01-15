import streamlit as st
from db_utils import insert_category, fetch_categories
import pandas as pd

def category_page():
    st.subheader("🔅〽️ Manage Categories")

    # Add Category Section
    st.subheader("🎯Add New Category")
    category_name = st.text_input("Category Name")
    category_description = st.text_area("Category Description")

    if st.button("Adding"):
        if category_name.strip():
            try:
                # Insert category into the database
                insert_category(category_name, category_description.strip())
                st.success("Category added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Category Name cannot be empty!")

    # View Categories Section
    st.subheader("View Existing Categories")
    # try:
    #     categories = fetch_categories()
    #     if categories:
    #         for category in categories:
    #             # st.write(f"**Category Name:** {category['Category_name']}")
    #             # st.write(f"**Description:** {category['description']}")
    #             # #st.markdown("---")
                
               
    #     else:
    #         st.info("No categories available.")
    # except Exception as e:
    #     st.error(f"Error fetching categories: {e}")

    try:
        categories = fetch_categories()
        if categories:
        # Create a DataFrame for displaying
            categories = {
                    "Category Name": [category['Category_name'] for category in categories],
                    "Description": [category['description'] for category in categories],                     
                }

            category_df = pd.DataFrame(categories)
            st.table(categories)
        else:
                st.write("No income records found for this user.")

    except Exception as e:
            st.error(f"An error occurred: {str(e)}")










    # try:
    #     categories = fetch_categories()
    #     if categories:
    #         for category in categories:
    #             # st.write(f"**Category Name:** {category['Category_name']}")
    #             # st.write(f"**Description:** {category['description']}")
    #             # #st.markdown("---")
                
    #             st.table(categories)
    #     else:
    #         st.info("No categories available.")
    # except Exception as e:
    #     st.error(f"Error fetching categories: {e}")