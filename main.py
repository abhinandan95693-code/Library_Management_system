from show_books import show
from add_books import add
from issue_book import issue
from return_book import return_book

def library():
    while True:
     print('\n1. Add Book')
     print('2. Show Book')
     print('3. Issue Book')
     print('4. Return Book')
     print('5. Exit')
     
     choice=int(input("Choose your option:"))
      
     if choice==1:  add()
     elif choice==2:    show()
     elif choice==3:    issue()
     elif choice==4:    return_book()
     elif choice==5:
         print("Thank you")
         break
     else:
         print("Enter a valid choice")

library()
    
     
    