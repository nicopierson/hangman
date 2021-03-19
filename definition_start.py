# practice assigning classes

class Book:
    '''assign title when initialized'''
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

class Newspaper:
    '''assign title when initialized'''
    def __init__(self, title):
        self.title = title

b1 = Book("Brave New World", "unknown", 843, 30.21)
b2 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
n1 = Newspaper("LA Times")

# print the titles
print(b1.title)
print(b2.title)
# get the price
print(f'Price of the book is: {b1.getprice()}')
b1.setdiscount(0.25)
print(f'Price after discount is: {b1.getprice()}')
# try to access __variable: can't because of data mangling
#print(b2.__secret)
# double underscores to make sure subclasses to not use the same name as an already used attribute

# can access with class
print(b2._Book__secret)

# instances
print(type(b1))
print(type(n1))

# compare two types
print(type(b1) == type(b2))
print(type(b1) == type(n1))

# use isinstance
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n1, Book))
print(isinstance(n1, object))