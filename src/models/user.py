import sqlite3

class UserModel:
    def __init__(self, conn):
        """Initialize the class with the database connection."""
        self.conn = conn

    def add_user(self, first_name, last_name, email, phone_number, address, created_at):
        """Add a new user to the database."""
        sql = '''INSERT INTO users (first_name, last_name, email, phone_number, address, created_at)
                 VALUES (?, ?, ?, ?, ?, ?)'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (first_name, last_name, email, phone_number, address, created_at))
            self.conn.commit()
            print("User added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")

    def get_all_users(self):
        """Retrieve all users from the database."""
        sql = '''SELECT * FROM users'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving users: {e}")
            return []

    def get_user_by_id(self, user_id):
        """Retrieve a specific user by their ID."""
        sql = '''SELECT * FROM users WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (user_id,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error retrieving user: {e}")
            return None

    def update_user(self, user_id, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        """Update an existing user's details."""
        sql = '''UPDATE users SET first_name = ?, last_name = ?, email = ?, phone_number = ?, address = ? WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (first_name, last_name, email, phone_number, address, user_id))
            self.conn.commit()
            print("User updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        """Delete a user by their ID."""
        sql = '''DELETE FROM users WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (user_id,))
            self.conn.commit()
            print("User deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")
