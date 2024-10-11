import sqlite3

class BookModel:
    def __init__(self, conn):
        """Initialize the class with the database connection."""
        self.conn = conn

    def add_book(self, title, author, genre, publication_date, isbn, quantity, available=True):
        """Add a new book to the database."""
        sql = '''INSERT INTO books (title, author, genre, publication_date, isbn, quantity, available)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (title, author, genre, publication_date, isbn, quantity, available))
            self.conn.commit()
            print("Book added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding book: {e}")

    def get_all_books(self):
        """Retrieve all books from the database."""
        sql = '''SELECT * FROM books'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving books: {e}")
            return []

    def get_book_by_id(self, book_id):
        """Retrieve a specific book by its ID."""
        sql = '''SELECT * FROM books WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (book_id,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error retrieving book: {e}")
            return None

    def update_book(self, book_id, title=None, author=None, genre=None, publication_date=None, isbn=None, quantity=None, available=None):
        """Update an existing book's details."""
        sql = '''UPDATE books SET title = ?, author = ?, genre = ?, publication_date = ?, isbn = ?, quantity = ?, available = ? WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (title, author, genre, publication_date, isbn, quantity, available, book_id))
            self.conn.commit()
            print("Book updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating book: {e}")

    def delete_book(self, book_id):
        """Delete a book by its ID."""
        sql = '''DELETE FROM books WHERE id = ?'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (book_id,))
            self.conn.commit()
            print("Book deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting book: {e}")
