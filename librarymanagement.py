

class library:
    def __init__(self,numberofbooks,books):
        self.numberofbooks = numberofbooks
        self.books=books

    def record(self):
        print("Record of books in the library:")
        for i in range(len(self.books)):
            self.numberofbooks+=1
            print(f"self {self.numberofbooks}: {self.books[i]}")
    def comparison(self):
        if self.numberofbooks==len(self.books):
            print("The library is updated")
            
        else:
            print("Some mismanagement in the library")
        if self.numberofbooks >= 20:
            print("The library is full")
            
           
        
books=input("enter the list of books:").split()
library=library(0,books)
library.record()
library.comparison()

