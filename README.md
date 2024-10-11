# BookFlow

## Management Rules
### Books
- A book must be able to be added to or removed from stock.
- The information of a book must be modifiable.
- A catalog must allow viewing all or a filtered set of books in stock.
- A product sheet must allow consulting the information of a chosen book.

### Users
- A user must be able to be added or deleted.
- The information of a user must be modifiable.
- A list must allow viewing all or a filtered set of users.
- A user profile must allow consulting the information of a chosen user.
- A user must be able to borrow multiple books.
- A user may be banned from borrowing after not returning three books for a duration of two months.

### Loans
- A loan must be able to be recorded with the following statuses:
  - "in progress"
  - "returned"
  - "not returned"
  - "overdue"
  - "error"
- A loan must not be deletable.
- The information of a loan must be modifiable.
- A list must allow viewing all or a filtered set of loans.
- A loan sheet must allow consulting the information of a loan.
- A loan must be considered "in progress" upon creation and for a duration of one month. The concerned book is destocked.
- A loan must change to "overdue" when returned after the expected return date. The book is restocked.
- A loan must change to "not returned" after the expected return date. The book is not restocked.
- A loan can be marked as "error" when an error occurs during the loan recording. The concerned book must be restocked.
- A loan must be marked as "returned" when the book is returned by the user. The book is restocked.
