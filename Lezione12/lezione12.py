class Book:
    def __init__(self, book_id,title,author,is_borrowed = False):
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = is_borrowed

    def borrow(self) -> None:
        self.is_borrowed = True
            
    def return_book(self) -> None:
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books: dict = {}

    def add_book(self, book_id: str, title: str, author: str): 
        book = Book(book_id,title,author)
        self.books[book_id] = book
        
    def borrow_book(self, book_id: str): 
        if book_id not in self.books:
            raise ValueError ("Book not found")
        x = self.books[book_id]
        if x.is_borrowed:
            raise ValueError ("Book is already borrowed")
        self.books[book_id].borrow()
        print("LIBRO PRESTATO")
    
    def return_book(self, book_id: str): 
        if self.books[book_id].is_borrowed == False:
            raise ValueError("Book not borrowed")
        x = self.books[book_id]
        self.books[book_id].return_book(x)
        print("LIBRO RESTITUITO")
    
    def get_books(self) -> list[Book]: 
        if len(self.books) == 0:
            raise ValueError ("No books in library")
        borrowed = []
        for x in self.books:
            borrowed.append(self.books[x].title)
        return borrowed
    

roma1 = Library()
libro1 = Book
roma1.add_book(2,"Percy Jackson","Per")
roma1.add_book(3,"Harry Potter","JKR")
roma1.add_book(1,"La fattoria degli animali","Orwell")
print(roma1.get_books())
roma1.borrow_book(2)
roma1.return_book(1)