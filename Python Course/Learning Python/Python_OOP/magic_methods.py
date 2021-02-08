# Magig functions

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price


# Use __str__ method to returning string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"


# Use  __repr__ method to return an obj representation
    def __repr__(self):
        return f"title = {self.title} by author = {self.author}, costs = {self.price}"

########### TEST ##########
b1 = Book("Brave new world", "leo Tolstoy", 39.95)
b2 = Book("War and Peace", "Theo", 60)

print(b1)
print(b2)
