## This module contains the user interface for the library system.
# It allows users to search for books, borrow books, and return books.
## Import the necessary functions from the admin module.
from admin import (
    find_book,
    load_library,
    save_library
)

## Search books by category.
## This function should return book IDs that match the given category.
def books_in_category(
    books,
    category
):
    target_cat = category.strip().lower()
    result_ids = []
    for book_id, book_info in books.items():
        if book_info["category"].lower() == target_cat:
            result_ids.append(book_id)
    return result_ids

## Search books by full or partial title.
## This function should return book IDs that match the given title or part of the title.
def search_by_title(
    books,
    search_text
):
    search_low = search_text.lower()
    matches = []
    for book_id, book_info in books.items():
        if search_low in book_info["title"].lower():
            matches.append(book_id)
    return matches

## Create logic to let users borrow books.
## The function should check if the book is available or on loan, or if the borrower name is provided.
## If the book is not found, then return "BOOK_NOT_FOUND"
## If the borrower name is empty, then return "EMPTY_NAME"
## If the book is not available, then return "NOT_AVAILABLE"
## If the book is successfully borrowed, then return "OK"
def borrow_book(
    books,
    loans,
    search_text,
    borrower
):
    borrower_clean = borrower.strip()
    if len(borrower_clean) == 0:
        return "EMPTY_NAME"

    book_id = find_book(books, search_text)
    if book_id is None:
        return "BOOK_NOT_FOUND"

    if not books[book_id]["available"]:
        return "NOT_AVAILABLE"

    books[book_id]["available"] = False
    loans.append({"book_id": book_id, "borrower": borrower_clean})
    return "OK"

## Create logic to let users return books.
## The function should check if the book is on loan, or if the borrower name is provided
## If the book is not found, then return "BOOK_NOT_FOUND"
## If the borrower name is empty, then return "EMPTY_NAME"
## If the book is not on loan, then return "NOT_ON_LOAN"
## If the book is successfully returned, then return "OK"
def return_book(
    books,
    loans,
    book_title,
    borrower
):
    borrower_clean = borrower.strip()
    if len(borrower_clean) == 0:
        return "EMPTY_NAME"

    book_id = find_book(books, book_title)
    if book_id is None:
        return "BOOK_NOT_FOUND"

    loan_index = None
    for idx, loan in enumerate(loans):
        if loan["book_id"] == book_id and loan["borrower"] == borrower_clean:
            loan_index = idx
            break
    if loan_index is None:
        return "NOT_ON_LOAN"

    del loans[loan_index]
    books[book_id]["available"] = True
    return "OK"

## The main function that runs the user interface for the library system.
## The function must first load the library data from a JSON file, then display a menu for the user to select options.
## The options include searching for books by title or category, borrowing a book, returning a book, and exiting the program.
## When the user selects an option, the corresponding function is called to perform the action.
## The program continues to display the menu until the user chooses to exit, at which point the library data is saved back to the JSON file.
## The main function should also handle invalid selections by displaying an error message and prompting the user to select again.
def main():
    lib_data = load_library("library.json")
    print("LIBRARY USER SYSTEM")
    while True:
        print("\n===== MENU =====")
        print("1. Search books by title")
        print("2. Search books by category")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            text = input("Enter title to search: ")
            res = search_by_title(lib_data["books"], text)
            print("Matching book IDs:", res)
        elif choice == "2":
            cat = input("Enter category to search: ")
            res = books_in_category(lib_data["books"], cat)
            print("Matching book IDs:", res)
        elif choice == "3":
            book_search = input("Enter book ID/title/author to borrow: ")
            name = input("Enter borrower name: ")
            status = borrow_book(lib_data["books"], lib_data["loans"], book_search, name)
            print(status)
        elif choice == "4":
            book_search = input("Enter book ID/title/author to return: ")
            name = input("Enter borrower name: ")
            status = return_book(lib_data["books"], lib_data["loans"], book_search, name)
            print(status)
        elif choice == "5":
            save_library(lib_data, "library.json")
            print("Saved library data, exiting.")
            break
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()
