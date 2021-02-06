########################
# Main Super classes
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    PERIODS = ("DAILY", "WEEKLY", "BIWEEKLY")

    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        if (not period in Periodical.PERIODS):
            raise ValueError(f"{period} is not a valid period type")
        else:
            self.period = period
        self.publisher = publisher


#########################
# Declaring 3 new classes

class Book(Publication):
    def __init__(self, title, price, author, pages):
        # this two can be replaced by super class
        # self.title = title
        # self.author = author
        super().__init__(title, price)
        self.author = author
        self.pages = pages
        


class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


### TESTING ###
b1 = Book("Brave New World", 2.99, 311, 29.95)
n1 = Newspaper("New York Times", 6.99, "DAILY",  "NYT Company")
m1 = Magazine("Scientific America", 5.99, "BIWEEKLY", "Spring Nature")

print(b1.author)
print(n1.publisher)
print(b1.price, n1.price, m1.price)
