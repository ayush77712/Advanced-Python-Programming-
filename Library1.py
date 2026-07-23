class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id} - {self.title} by {self.author} ({status})"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.patron_id} - {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    def issue_book(self, book_id, patron_id):
        if book_id in self.books and patron_id in self.patrons:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.available:
                book.available = False
                patron.borrowed_books.append(book)
                print(f"Book '{book.title}' issued to {patron.name}.")
            else:
                print("Book is already issued.")
        else:
            print("Invalid Book ID or Patron ID.")

    def return_book(self, book_id, patron_id):
        if book_id in self.books and patron_id in self.patrons:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book in patron.borrowed_books:
                patron.borrowed_books.remove(book)
                book.available = True
                print(f"Book '{book.title}' returned successfully.")
            else:
                print("This patron did not borrow the book.")
        else:
            print("Invalid Book ID or Patron ID.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)



library = Library()


library.add_book(Book(101, "Python Programming", "Guido van Rossum"))
library.add_book(Book(102, "Data Structures", "Mark Allen"))


library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Priya"))


library.display_books()


library.issue_book(101, 1)


library.display_books()


library.return_book(101, 1)

library.display_books()
