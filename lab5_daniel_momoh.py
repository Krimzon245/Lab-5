# Name: Daniel Momoh
# Student Number: 041114358
# Date: 2025-06-09

class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available Copies: {self.available_copies}")
        print("-" * 20)  # Separator for better readability

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Book '{self.title}' borrowed successfully.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.available_copies += 1
        print(f"Book '{self.title}' returned successfully.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():  # Case-insensitive search
                return book
        return None  # Return None if the book is not found

    def display_all_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                book.display_info()



# Demonstrate the functionality:
library = Library()

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978", 5)
book2 = Book("Pride and Prejudice", "Jane Austen", "979", 3)
book3 = Book("1984", "George Orwell", "977", 2)
book4 = Book("The Lord of the Rings", "J.R.R. Tolkien", "980", 0)  # Example: Book with no copies

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)


while True:  # Main loop for user interaction
    print("\n--- Library Menu ---")
    print("1. Display all books")
    print("2. Search for a book by title")
    print("3. Borrow a book")  # Added borrow option
    print("4. Return a book")  # Added return option
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.display_all_books()
    elif choice == '2':
        title = input("Enter the title to search: ")
        found_book = library.find_book_by_title(title)
        if found_book:
            print("Book found:")
            found_book.display_info()
        else:
            print("Book not found.")
    elif choice == '3':  # Borrow book
        title = input("Enter the title of the book to borrow: ")
        found_book = library.find_book_by_title(title)
        if found_book:
            found_book.borrow_book()
        else:
            print("Book not found.")
    elif choice == '4':  # Return book
        title = input("Enter the title of the book to return: ")
        found_book = library.find_book_by_title(title)
        if found_book:
            found_book.return_book()
        else:
            print("Book not found.")
    elif choice == '5':
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the library system!")