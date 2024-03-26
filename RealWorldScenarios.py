"""
Task 1: Library System Enhancement
    - Add functionality to insert new books into library.
    - Ensure that adding a duplicate book is handled appropriately.
"""
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


def add_books(catalog):
    title = input("Enter the title of the book: ").title()
    author = input("Enter the author's name: ").title()
    new_book_info = (title, author)
    if new_book_info in catalog:
        print("That book is already in the library.")
    else:
        catalog.append(new_book_info)


if __name__ == "__main__":
    add_books(library)
    print(library)
