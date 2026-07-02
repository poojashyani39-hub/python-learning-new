# List to store all books
books = []


# Function to add a new book
def add_book():

    # Validate Book ID
    while True:
        book_id = input("Enter Book ID: ").strip()

        if book_id == "":
            print("Book ID cannot be empty.")
        elif not book_id.isdigit():
            print("Book ID should contain only digits.")
        else:
            break

    # Validate Book Name
    while True:
        book_name = input("Enter Book Name: ").strip()

        if book_name == "":
            print("Book Name cannot be empty.")
        else:
            break

    # Validate Author Name
    while True:
        author_name = input("Enter Author Name: ").strip()

        if author_name == "":
            print("Author Name cannot be empty.")
        else:
            break

    # Create a dictionary for one book
    book = {
        "book_id": book_id,
        "book_name": book_name,
        "author_name": author_name,
        "status": "Available"
    }

    # Add book to the list
    books.append(book)

    print("Book Added Successfully.")


# Function to search a book
def search_book():

    # Check if the list is empty
    if len(books) == 0:
        print("No books found.")
        return

    search_id = input("Enter Book ID to Search: ").strip()

    found = False

    # Search book using Book ID
    for book in books:
        if book["book_id"] == search_id:

            print("\nBook Found")
            print("Book ID     :", book["book_id"])
            print("Book Name   :", book["book_name"])
            print("Author Name :", book["author_name"])
            print("Status      :", book["status"])

            found = True
            break

    if found == False:
        print("Book not found.")


# Function to issue a book
def issue_book():

    if len(books) == 0:
        print("No books found.")
        return

    book_id = input("Enter Book ID to Issue: ").strip()

    found = False

    # Find the book
    for book in books:
        if book["book_id"] == book_id:

            # Check current status
            if book["status"] == "Issued":
                print("Book is already issued.")
            else:
                book["status"] = "Issued"
                print("Book Issued Successfully.")

            found = True
            break

    if found == False:
        print("Book not found.")


# Function to return a book
def return_book():

    if len(books) == 0:
        print("No books found.")
        return

    book_id = input("Enter Book ID to Return: ").strip()

    found = False

    # Search the book
    for book in books:
        if book["book_id"] == book_id:

            # Check status before returning
            if book["status"] == "Available":
                print("Book is already available.")
            else:
                book["status"] = "Available"
                print("Book Returned Successfully.")

            found = True
            break

    if found == False:
        print("Book not found.")


# Function to display all books
def display_books():

    if len(books) == 0:
        print("No books found.")
        return

    print("\n----- Book List -----")

    # Display each book
    for book in books:
        print("Book ID     :", book["book_id"])
        print("Book Name   :", book["book_name"])
        print("Author Name :", book["author_name"])
        print("Status      :", book["status"])
        print("--------------------------")


# Main Menu
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Call Add Book Function
    if choice == "1":
        add_book()

    # Call Search Book Function
    elif choice == "2":
        search_book()

    # Call Issue Book Function
    elif choice == "3":
        issue_book()

    # Call Return Book Function
    elif choice == "4":
        return_book()

    # Call Display Books Function
    elif choice == "5":
        display_books()

    # Exit the program
    elif choice == "6":
        print("Thank you for using Library Management System.")
        break

    # Invalid menu option
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")