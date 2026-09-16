import json

## This function should load the library data from a JSON file and return it as a suitable Python data structure.
def load_library(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

## This function should save the library data to a JSON file.
## This function does not need to return anything, but it should ensure that the data is saved correctly to the specified file.
def save_library(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

## This function should find a book by its title, author, or ID.
## If the book is found, it should return the book ID.
## If the book is not found, it should return None.
def find_book(books, search_text):
    cleaned_search = search_text.strip().lower()
    for book_id, book_info in books.items():
        if book_id.lower() == cleaned_search:
            return book_id
        if book_info["title"].lower() == cleaned_search:
            return book_id
        if book_info["author"].lower() == cleaned_search:
            return book_id
    return None

## This function should display the list of books in a user-friendly format.
## It should show the book ID, title, category, and availability status (available or on loan).
## If the book is available, it should display "AVAILABLE", and if it is on loan, it should display "ON LOAN".
## The function should not return anything, but it should print the information to the console.
## The heading for this display should be "BOOK CATALOGUE".
def display_books(books):
    print("BOOK CATALOGUE")
    print("-" * 60)
    for book_id, book_info in books.items():
        status = "AVAILABLE" if book_info["available"] else "ON LOAN"
        print(f"{book_id} | {book_info['title']} | {book_info['category']} | {status}")

## This function should display the list of current loans in a user-friendly format.
## It should show the book ID, title, and the name of the borrower.
## The heading for this display should be "CURRENT LOANS".
## The function should not return anything, but it should print the information to the console.
def display_loans(loans, books):
    print("CURRENT LOANS")
    print("-" * 60)
    for loan in loans:
        book_id = loan["book_id"]
        borrower = loan["borrower"]
        title = books[book_id]["title"]
        print(f"{book_id} | {title} | Borrower: {borrower}")

## This function should calculate and return the library statistics
## The statsitics should include the total number of books, the number of available books, and the number of borrowed books.
## The function should return these three values in the order: total, available, borrowed. Use a suitable data structure to return these values, such as a tuple or a dictionary.
def library_statistics(books):
    total = len(books)
    available = sum(1 for b in books.values() if b["available"])
    borrowed = total - available
    return (total, available, borrowed)

## This function should display the library statistics in a user-friendly format.
## It should first load the library data from a JSON file,
## Then calculate the statistics, and finally print the information to the console.
## The heading for this display should be "LIBRARY STATISTICS".
## It should print the total number of books, the number of available books, and the number of borrowed books.
## The function should not return anything, but it should print the information to the console.
def main():
    lib_data = load_library("library.json")
    print("LIBRARY ADMINISTRATION")
    print("=" * 60)
    print(f"Library: {lib_data['library']['name']}")
    print(f"Branch: {lib_data['library']['branch']}")
    print(f"Year: {lib_data['library']['year']}")
    print(f"Categories: {', '.join(lib_data['categories'])}")

    display_books(lib_data["books"])
    display_loans(lib_data["loans"], lib_data["books"])

    print("STATISTICS")
    print("-" * 60)
    total, available, borrowed = library_statistics(lib_data["books"])
    print(f"Total books: {total}")
    print(f"Available: {available}")
    print(f"Borrowed: {borrowed}")

if __name__ == "__main__":
    main()
