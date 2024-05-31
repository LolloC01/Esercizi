from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, base: float, hight: float) -> None:
        super().__init__()
        self.base = base
        self.hight = hight

    def perimeter(self):
        return self.base*2+self.hight*2
    
    def area(self):
        return self.base*self.hight
    
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 2*pi*self.radius
    
    def area(self):
        return pi*(self.radius*self.radius)


rettangolo = Rectangle(10,5)
print(rettangolo.area())
print(rettangolo.perimeter())
cerchio = Circle(10)
print(cerchio.area())
print(cerchio.perimeter())


class MathOperations:

    @staticmethod
    def add(a,b) -> float:
        return a + b
    
    @staticmethod
    def multiply(a,b) -> float:
        return a * b
    

print(MathOperations.add(10,20))
print(MathOperations.multiply(3,10))

class Book:
    def __init__(self,title,author,isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"title: {self.title}\nauthor: {self.author}\nisbn: {self.isbn}"
    
    @classmethod 
    def from_string(cls, book_str: str):
        l: list = book_str.split(sep=", ")
        new_book = Book(l[0],l[1],l[2])
        return new_book
    


class Member:
    def __init__(self,name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"name: {self.name}\nid: {self.member_id}"

    @classmethod 
    def from_string(cls, member_str):
        l: list = member_str.split(sep=", ")
        new_member = Member(l[0],l[1])
        return new_member
    

class Library:
    total_books = 0
    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            Library.total_books += 1

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            Library.total_books -= 1

    def register_member(self, member):
        if member not in self.members:
            self.members.append(member)

    def lend_book(self, book, member):
        if member not in self.members:
            raise ValueError("Membro non registrato")
        if book not in self.books:
            raise ValueError("Libro non presente")
        
    __str__ method to return a string representation of the library with the list of books and members.

    @classmethod library_statistics(cls) to print the total number of books.
