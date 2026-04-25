from utils import books
def add():
    book_name=input("Enter the book name you want to add to the library: ")
    books.append(book_name)
    print(f"You added: {book_name}")