class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_brrowed = False
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")
book1 = Book("Harry Potter, J.K Rowling")
book2 = Book("The Jungle Book" , "Rudyard Kipling")
book3 = Book("wings of Fire" , "A.P.J Abdul Kalem")

book1.borrow()
book2.borrow()
book1.borrow()
book1.return_book()
book2.return_book()
book3.borrow()
book3.return_book()
        