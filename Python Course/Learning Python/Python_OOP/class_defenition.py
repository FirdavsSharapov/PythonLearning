
# TODO: create a basic class
class Book():
    # This how we define Properties at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # Create a method that return book typelist. Class method decorator
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    
    def __init__(self, title, author, page_count, price, booktype): # initiliziong 
        self.title = title
        self.author = author
        self.page_count = page_count
        self.price = price
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
    
    # Create instance method
    def get_price (self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    # Discount function
    def discount(self, amount):
        self._discount = amount


class NewsPaper():
    def __init__(self, paper_name):
        self.paper_name = paper_name
        
        


# TODO: Create instance of the class

b1 = Book("Brave new world", "leo Tolstoy", 1225, 39.95, "HARDCOVER")
b2 = Book("War and Peace", "Theo", 200, 60, "HARDCOVER")
b2.discount(0.2)


# TODO: print the class and property
print (b2.get_price())
print (b2.title)
print ("Books types are:", Book.getbooktypes()) 

