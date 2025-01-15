import pyodbc

# Database connection
file_path = r"F:\Apps\Db.accdb"  # Replace with your path

def create_connection():
    conn = pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f'DBQ={file_path};'
    )
    return conn

# User authentication
def authenticate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, role FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Add a new user to user table
def add_user(username, password, role):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        return True
    except Exception as e:
        return str(e)
    finally:
        conn.close()

# Display user form user table.
def fetch_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, role FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Delete a user From user table.
def delete_user(username):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        return True
    except Exception as e:
        return str(e)
    finally:
        conn.close()

# Insert a new income record into the Income table with user_id

def add_income(amount, iName, IncomeDate, description, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        print("Inserting income into database...")
        query = """
            INSERT INTO Income (Amount, iName, IncomeDate, description, user_id)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (amount, iName, IncomeDate, description, user_id))
        conn.commit()
        print(f"Income record added successfully with Amount: {amount}, IncomeName: {iName}")
        return True
    except Exception as e:
        print(f"Error inserting income: {e}")
        return str(e)
    finally:
        conn.close()

def fetch_user_incomes(user_id):
    """Fetch all income records for a specific user."""
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Income WHERE user_id = ?", (user_id,))
        columns = [column[0] for column in cursor.description]  # Extract column names
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]  # Convert rows to dictionaries
    finally:
        conn.close()

# Insert a new expense record into the Expenses table with user_id
def insert_expense(tdate, amount, description, category_id, user_id):
    """Insert a new expense record into the Expenses table."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO Expenses (TransactionDate, Amount, Description, CategoryID, user_id)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (tdate, amount, description, category_id, user_id))
        conn.commit()
    except Exception as e:
        raise Exception(f"Error inserting record: {e}")
    finally:
        conn.close()
# Fetch expense records for a specific user
def fetch_user_expenses(user_id):
    """Fetch expense records for a specific user based on user_id"""
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Expenses WHERE user_id = ?", (user_id,))
        columns = [column[0] for column in cursor.description]  # Get column names
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]  # Convert to dictionary
    finally:
        conn.close()

# Insert a new category into the Category table
def insert_category(Category_name, Description):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Category (Category_name, description) VALUES (?, ?)", (Category_name, Description))
        conn.commit()
        return True
    except Exception as e:
        return str(e)
    finally:
        conn.close()

# Fetch all categories from the Category table
def fetch_categories():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, Category_name, description FROM Category")
        categories = cursor.fetchall()
        # Return categories in a list of dictionaries
        return [{"id": row[0], "Category_name": row[1], "description": row[2]} for row in categories]
    except Exception as e:
        raise Exception(f"Error fetching categories: {e}")
    finally:
        conn.close()


# Fetch all summary from the expenses on tables
def fetch_summary(user_id, month, year):
    """Fetch income, expense totals, and detailed expenses for a given user, month, and year."""
    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Fetch total income for the specific user
        income_query = """
            SELECT SUM(Amount) FROM Income
            WHERE user_id = ? AND MONTH(IncomeDate) = ? AND YEAR(IncomeDate) = ?
        """
        cursor.execute(income_query, (user_id, month, year))
        total_income = cursor.fetchone()[0] or 0.0
        total_income = float(total_income)  # Convert to float if necessary

        # Fetch total expenses for the specific user
        expense_query = """
            SELECT SUM(Amount) FROM Expenses
            WHERE user_id = ? AND MONTH(TransactionDate) = ? AND YEAR(TransactionDate) = ?
        """
        cursor.execute(expense_query, (user_id, month, year))
        total_expenses = cursor.fetchone()[0] or 0.0
        total_expenses = float(total_expenses)  # Convert to float if necessary

        # Fetch detailed expenses for the specific user
        detailed_expenses_query = """
            SELECT 
                Expenses.Amount AS expense_amount, 
                Expenses.TransactionDate AS transaction_date, 
                Category.Category_Name AS category_name
            FROM Expenses
            INNER JOIN Category ON Expenses.CategoryID = Category.ID
            WHERE Expenses.user_id = ? AND MONTH(TransactionDate) = ? AND YEAR(TransactionDate) = ?
        """
        cursor.execute(detailed_expenses_query, (user_id, month, year))
        detailed_expenses = [
            {
                "amount": float(row.expense_amount),  # Ensure expense_amount is converted to float
                "transaction_date": row.transaction_date,
                "category": row.category_name,
            }
            for row in cursor.fetchall()
        ]

        return total_income, total_expenses, detailed_expenses

    except Exception as e:
        raise Exception(f"Error fetching summary: {e}")
    finally:
        conn.close()

# Delete an income record
def delete_income(income_id):
    """Delete an income record."""
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Income WHERE ID = ?", (income_id,))
        conn.commit()
    finally:
        conn.close()

# Update an income record
def update_income(income_id, iName, Amount, IncomeDate, description):
    """Update an income record."""
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Income
            SET iName = ?, Amount = ?, IncomeDate = ?, description = ?
            WHERE ID = ?
        """, (iName, Amount, IncomeDate, description, income_id))
        conn.commit()
    finally:
        conn.close()



