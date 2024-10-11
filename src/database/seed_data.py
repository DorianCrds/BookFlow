import sqlite3
from datetime import date


from src.models.book import BookModel
from src.models.user import UserModel
from src.models.loan import LoanModel


def seed_data():
    # Step 1: Connect to the database
    conn = sqlite3.connect("src/database/database.db")

    # Step 2: Create instances of the models
    book_model = BookModel(conn)
    user_model = UserModel(conn)
    loan_model = LoanModel(conn)

    user_model.add_user("John", "Doe", "john.doe@example.com", "123456789", "123 Main St", date.today())
    user_model.add_user("Jane", "Smith", "jane.smith@example.com", "987654321", "456 Elm St", date.today())

    book_model.add_book("1984", "George Orwell", "Dystopian", "1949-06-08", "9780451524935", 5, True)
    book_model.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", "1960-07-11", "9780060935467", 3, True)
    book_model.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "1925-04-10", "9780743273565", 4, True)

    # Example loan: John Doe borrows "1984"
    loan_model.add_loan(1, 1, date.today(), date(2024, 11, 10), "On Loan")

    # Example loan: Jane Smith borrows "To Kill a Mockingbird"
    loan_model.add_loan(2, 2, date.today(), date(2024, 11, 15), "On Loan")

    print("Sample data inserted successfully!")

    # Close the connection
    conn.close()


if __name__ == "__main__":
    seed_data()
