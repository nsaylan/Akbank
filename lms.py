class Library:
    def __init__(self):
        try:
            self.file_path = "books.txt"
            self.file = open(self.file_path, "a+")
        except IOError as e:
            print(f"Error opening the file: {e}")

    def __del__(self):
        try:
            self.file.close()
        except Exception as e:
            print(f"Error closing the file: {e}")
            
    def list_books(self):
        try:
            self.file.seek(0)
            lines = self.file.read().splitlines()
            if not lines:
                print("There are no books in the library.")
            else:        
                for line in lines:
                    book_info = line.split(',')
                    print(f"Book: {book_info[0]}, Author: {book_info[1]}")
        except Exception as e:
            print(f"Error listing books: {e}")
            
    def add_book(self):
        try:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            # Validate release year
            while True:
                release_year = input("Enter release year: ")
                if release_year.isdigit() and len(release_year) == 4:
                    break
                else:
                    print("Invalid release year. Please enter a valid 4-digit year.")
                
         # Validate number of pages        
            while True:
                num_pages = input("Enter number of pages: ")
                if num_pages.isdigit() and int(num_pages) > 0:
                    break
                else:
                    print("Invalid number of pages. Please enter a valid positive integer.")


            book_info = f"{title},{author},{release_year},{num_pages}\n"
            self.file.write(book_info)
            print(f"Book '{title}' added successfully.")
        except Exception as e:
            print(f"Error adding book: {e}")
            
    def remove_book(self):
        try: 
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
        except Exception as e:
            print(f"Error removing book: {e}")


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
