import sqlite3

class LoanModel:
    def __init__(self, conn):
        """Initialize the class with the database connection."""
        self.conn = conn

    def add_loan(self, book_id, user_id, loan_date, expected_return_date, status="in progress", actual_return_date=None):
        """Add a new loan to the database. The book is destocked."""
        sql = '''INSERT INTO loan (book_id, user_id, loan_date, expected_return_date, actual_return_date, status)
                 VALUES (?, ?, ?, ?, ?, ?)'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (book_id, user_id, loan_date, expected_return_date, actual_return_date, status))
            self.conn.commit()

            # Decrease book quantity (destock)
            self.update_book_stock(book_id, -1)

            print("Loan added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding loan: {e}")

    def get_all_loans(self):
        """Retrieve all loans from the database."""
        sql = '''SELECT * FROM loan'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving loans: {e}")
            return []

    def get_loan_by_id(self, loan_id):
        """Retrieve a specific loan by its ID."""
        sql = '''SELECT * FROM loan WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (loan_id,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error retrieving loan: {e}")
            return None

    def update_loan(self, loan_id, book_id=None, user_id=None, loan_date=None, expected_return_date=None, actual_return_date=None, status=None):
        """Update an existing loan's details. Handle stock changes based on the loan's status."""
        sql = '''UPDATE loan SET book_id = ?, user_id = ?, loan_date = ?, expected_return_date = ?, actual_return_date = ?, status = ? WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (book_id, user_id, loan_date, expected_return_date, actual_return_date, status, loan_id))
            self.conn.commit()

            # Restock the book when the loan is returned or marked as error
            if status in ["returned", "error"]:
                self.update_book_stock(book_id, 1)

            print("Loan updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating loan: {e}")

    def update_book_stock(self, book_id, change):
        """Update book stock by adjusting the quantity."""
        sql = '''UPDATE books SET quantity = quantity + ? WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (change, book_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating book stock: {e}")

    # Loan deletion is disallowed according to management rules
