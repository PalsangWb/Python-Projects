"""
    Implement a student library system using OOPs where students can borrow a book from the list of books.
    Create a seperate library and student class. Your program must be menu driven. You are free to choose methods and
    attributes of your choice to implement this functionality.
"""
class Library:
    def __init__(self, books):
        self.book = books
        
    def display_All_Books(self):
        if not self.book:
            print("Sorry we are out of books.")
        else:
            print("===Welcome to our library===\n")
            for book in self.book:
                print(f"* {book}")

    def request_Book(self, book_name):
        if book_name in self.book:
            print(f"{book_name} book requesting.")
            print("Approving...")
            print("Your request has been approved. \n")
            self.book.remove(book_name)
            return True
        else:
            print(f" Sorry {book_name} book has been issued to someone.")
            return False
        
    def return_Book(self, book_name):
        print(f"Book returning: {book_name}")
        print("Verifying...")
        print("Verify complete. Thanks for returning the book. \n")
        self.book.append(book_name)

class Student:
    def return_Book(self):
        book_name = input("Enter the book name: ")
        return book_name

    def request_Book(self):
        book_name = input("Enter the book name: ")
        return book_name

def main():
    library = Library(["Rich dad poor dad", "The Lords of Easy Money"])
    
    student = Student()

    while True:
        print("\n ===*Welcome to our library===*")
        print("1. Display all books")
        print("2. Return book")
        print("3. Request book")
        print("4. Exit from library")

        try:
            choose = int(input("Enter your options:"))
        except ValueError:
            print("Invalid choices. Make sure to choose numbers from 1 to 4.")
            continue

        if choose == 1:
            library.display_All_Books()
        elif choose == 2:
            book_name = student.return_Book()
            library.return_Book(book_name)
        elif choose == 3:
            book_name = student.request_Book()
            library.request_Book(book_name)
        elif choose == 4:
            print("Thank you for choosing our library.")
            break
        else:
            print("Invalid choices")

if __name__ == "__main__":
    main()

            