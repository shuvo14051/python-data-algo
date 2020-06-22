class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("Available book:")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available.")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thank you!!")


class Customer:
    def requestBook(self):
        print("Enter the name of the book you want to borrow:")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the book you are returning:")
        self.book = input()
        return self.book

library = Library(['abc', 'bcd', 'cba'])
customer = Customer()

print("Enter 1 to display the available book")
print("Enter 2 to request for a book")
print("Enter 3 to return a book")
print("Enter 4 to quit")

while True:
    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()

