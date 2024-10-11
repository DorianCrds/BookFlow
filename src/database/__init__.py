import sqlite3
from sqlite3 import Error

class Db:
    def __init__(self, db_file):
        """Initialize the class with the path to the database file."""
        self.db_file = db_file
        self.conn = None
        self.create_connection()
        self.initialize_db()

    def create_connection(self):
        """Create a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"Successfully connected to the database '{self.db_file}'")
        except Error as e:
            print(f"Error connecting to the database: {e}")

    def initialize_db(self):
        """Create the tables if they do not exist."""
        if self.conn is not None:
            try:
                self.create_tables()
            except Error as e:
                print(f"Error initializing the database: {e}")
        else:
            print("Database connection not established.")

    def create_tables(self):
        """Create the 'books', 'loan', and 'users' tables."""
        create_books_table = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL,
            publication_date DATE,
            isbn TEXT UNIQUE NOT NULL,
            quantity INTEGER NOT NULL,
            available BOOLEAN DEFAULT TRUE
        );
        """

        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone_number TEXT NOT NULL,
            address TEXT,
            created_at DATE NOT NULL
        );
        """

        create_loan_table = """
        CREATE TABLE IF NOT EXISTS loan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            loan_date DATE NOT NULL,
            expected_return_date DATE NOT NULL,
            actual_return_date DATE,
            status TEXT NOT NULL,
            FOREIGN KEY (book_id) REFERENCES books (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
        """

        try:
            cursor = self.conn.cursor()
            cursor.execute(create_books_table)
            cursor.execute(create_users_table)
            cursor.execute(create_loan_table)
            self.conn.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def close_connection(self):
        """Close the connection to the database."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Create an instance of the database
    db = Db("library.db")
    # Close the connection
    db.close_connection()
