"""
Library Management System
Author: Sakshi N
Description: CLI-based system using Python, OOP, and JSON storage
"""
import json
import os

class Library:
    def __init__(self, file_name="library.json"):
        self.file_name = file_name
        self.books = []
        self.issued_books = {}
        self.load_data()

    def load_data(self):
        """Load data from JSON file"""
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = json.load(file)
                self.books = data.get("books", [])
                self.issued_books = data.get("issued_books", {})
        else:
            self.save_data()

    def save_data(self):
        """Save data to JSON file"""
        data = {
            "books": self.books,
            "issued_books": self.issued_books
        }
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_book(self, book_name):
        if book_name in self.books:
            print("⚠️ Book already exists!")
        else:
            self.books.append(book_name)
            self.save_data()
            print("✅ Book added!")

    def view_books(self):
        if not self.books:
            print("📭 No books available.")
        else:
            print("\n📚 Available Books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.lower()]
        if results:
            print("\n🔍 Search Results:")
            for book in results:
                print(f"- {book}")
        else:
            print("❌ No matching books found.")

    def issue_book(self, book_name, user):
        if book_name in self.books:
            self.books.remove(book_name)
            self.issued_books[book_name] = user
            self.save_data()
            print(f"📖 Book issued to {user}")
        else:
            print("❌ Book not available!")

    def return_book(self, book_name):
        if book_name in self.issued_books:
            self.books.append(book_name)
            user = self.issued_books.pop(book_name)
            self.save_data()
            print(f"🔄 Book returned by {user}")
        else:
            print("❌ This book was not issued!")

    def view_issued_books(self):
        if not self.issued_books:
            print("📭 No issued books.")
        else:
            print("\n📕 Issued Books:")
            for book, user in self.issued_books.items():
                print(f"{book} → Issued to {user}")


def main():
    lib = Library()

    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Issued Books")
        print("7. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                book = input("Enter book name: ")
                lib.add_book(book)

            elif choice == 2:
                lib.view_books()

            elif choice == 3:
                keyword = input("Enter keyword: ")
                lib.search_book(keyword)

            elif choice == 4:
                book = input("Enter book name: ")
                user = input("Enter user name: ")
                lib.issue_book(book, user)

            elif choice == 5:
                book = input("Enter book name: ")
                lib.return_book(book)

            elif choice == 6:
                lib.view_issued_books()

            elif choice == 7:
                print("👋 Thank you!")
                break

            else:
                print("⚠️ Invalid choice!")

        except ValueError:
            print("❌ Please enter a valid number!")


if __name__ == "__main__":
    main()
