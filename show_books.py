from utils import books
def show():
    if len(books)==0:
        print("Books are not available in the library.")
    else:
        for _ in books:
            print(_)