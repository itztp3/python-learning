books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    book = {
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully!")

def view_books():
    if not books:
        print("No books in the library.")
        return

    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        print(
            book["title"],
            "|", book["author"],
            "|", status
        )

def borrow_book():
    title = input("Enter the book title to borrow: ")

    for book in books:
        if book["title"].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully!")
            else:
                print("This book is already borrowed.")
            return

    print("Book not found.")

while True:
    print("\n--- Library Management System ---")
    print("1. Add book")
    print("2. View books")
    print("3. Borrow book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        borrow_book()
    elif choice == "4":
        print("Library system closed.")
        break
    else:
        print("Invalid choice.")
