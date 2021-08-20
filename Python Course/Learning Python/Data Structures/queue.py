class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ This method takes an item and iserts that item into the 0th
        index of the list that is representing the queue.

        The runtime is O(n), or liniar time, becasue inserting into the
        0th index of the list forces all the other items in the list
        to move one index to the right.
        """
        self.items.insert(0, item)

    def dequeue(self, item):
        """This method return and removes the front-most item of the queue, which
        is represented by the last item in the list.

        The runttime is O(1), or constant time, because indexing to the end of the 
        a list happens in constant time.
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self, item):
        """This method return the last item of the list which is represents
        the front-most item in the list.
        The run time is O(1), or constant time, because indexing to the end of the list.
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self, item):
        """Returns the size of the queue, which is represents by the leght
        of the list.
        The runtime is O(1), or constant time, because we're only returning the 
        leght.
        """
        return len(self.items)

    def is_empty(self, item):
        """Return a boolean that represents if list is empty or not.
        The runtime is O(1), or constant because it checks similarity 
        """
        return self.items == []
