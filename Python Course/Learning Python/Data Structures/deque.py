class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """This method takes an item as  a parameter and inserts it 
        to the list that of representing the Deque.

        The runtime is linear, or O(n), because every time you insert 
        into the front of a list, all the other items in the list need to shift
        one position to the right. 
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """This method takes an item as  a parameter and inserts it 
        to the end of a list that of representing the Deque.

        The runtime is o(1), or constant because appending to the end of a list happens 
        in constant time.
        """
        self.items.append()

    def remove_front(self, item):
        pass

    def remove_rear(self, item):
        pass

    def peek_front(self, item):
        pass

    def peek_rear(self, item):
        pass

    def size(self, item):
        pass

    def is_empty(self):
        pass
