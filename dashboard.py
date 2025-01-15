import streamlit as st
from db_utils import create_connection, fetch_all_users, delete_user, add_user

def dashboard_page():
    if "user" in st.session_state and st.session_state["user"]["role"] == "admin":
        st.subheader("🔅〽️ Admin Dashboard")

        # Fetch users from the database
        users = fetch_all_users()

        if users:
            # Table headers
            st.markdown("""
                <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                th, td {
                    border: 2px solid black;
                    text-align: right;
                    padding: 8px;
                }
                th {
                    background-color: black;
                }
                </style>
                <table>
                    <thead>
                        <tr>
                            <th>Username</th>
                            <th>Role</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                </table>
            """, unsafe_allow_html=True)

            # Iterate over users and display rows with Streamlit widgets
            for user in users:
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                with col1:
                    st.text(user[1])  # Username
                with col2:
                    st.text(user[2])  # Role
                with col3:
                    if st.button("Edit", key=f"edit_{user[0]}"):
                        st.session_state["edit_user"] = user
                with col4:
                    if st.button("Delete", key=f"delete_{user[0]}"):
                        delete_user(user[1])
                        st.success(f"User {user[1]} deleted successfully!")
                        st.experimental_rerun()  # Refresh the page

        else:
            st.info("No users found in the database.")

        # Edit user modal
        if "edit_user" in st.session_state:
            st.subheader("Edit User")
            user_to_edit = st.session_state["edit_user"]
            new_username = st.text_input("Username", value=user_to_edit[1])
            new_role = st.selectbox("Role", ["user", "admin"], index=0 if user_to_edit[2] == "user" else 1)

            if st.button("Save Changes"):
                try:
                    conn = create_connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE users SET username = ?, role = ? WHERE id = ?",
                        (new_username, new_role, user_to_edit[0])
                    )
                    conn.commit()
                    conn.close()
                    st.success("User details updated successfully!")
                    del st.session_state["edit_user"]
                    st.experimental_rerun()  # Refresh the page
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        st.warning("This page is for admins only. Access restricted.")



# import streamlit as st
# from db_utils import create_connection, fetch_all_users, delete_user, add_user
# from time import sleep

# def dashboard_page():
#     if "user" in st.session_state and st.session_state["user"]["role"] == "admin":
#         st.subheader("🔅〽️ Admin Dashboard")
    
#         users = fetch_all_users()

#         if users:
#             for user in users:
#                 col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
#                 col1.text(user[1])  # Username
#                 col2.text(user[2])  # Role
#                 if col3.button("Edit", key=f"edit_{user[0]}"):
#                     st.session_state["edit_user"] = user
#                 if col4.button("Delete", key=f"delete_{user[0]}"):
#                     delete_user(user[1])
#                     st.success(f"User {user[1]} deleted successfully!")
#                     # Trigger page reload using query_params
#                     #st.set_query_params()
#                     #st.experimental_update_query_params(refresh="true")
#                     st.stop()  # Stops further execution to reload the page
#         else:
#             st.info("No users found in the database.")

#         # Edit user modal
#         if "edit_user" in st.session_state:
#             st.subheader("Edit User")
#             user_to_edit = st.session_state["edit_user"]
#             new_username = st.text_input("Username", value=user_to_edit[1])
#             new_role = st.selectbox("Role", ["user", "admin"], index=0 if user_to_edit[2] == "user" else 1)
            
#             if st.button("Save Changes"):
#                 try:
#                     conn = create_connection()
#                     cursor = conn.cursor()
#                     cursor.execute(
#                         "UPDATE users SET username = ?, role = ? WHERE id = ?",
#                         (new_username, new_role, user_to_edit[0])
#                     )
#                     conn.commit()
#                     conn.close()
#                     st.success("User details updated successfully!")
#                     del st.session_state["edit_user"]
#                     # Trigger page reload using query_params
#                     st.experimental_update_query_params(refresh="true")
#                     st.stop()  # Stops further execution to reload the page
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#     else:
#         st.warning("Welcome to App this Page is admins only, Access restricted .")
            
            
 