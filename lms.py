class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        if not lines:
            print("There are no books in the library.")
        else:        
            for line in lines:
                book_info = line.split(',')
                print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        
        book_removed = False

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)
            else:
                book_removed = True

        if book_removed:
            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"There is no such a book with title '{title_to_remove}'.")


# Creating an object named "lib" with "Library" class
lib = Library()

# Creating a menu to interact with the "lib" object
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
