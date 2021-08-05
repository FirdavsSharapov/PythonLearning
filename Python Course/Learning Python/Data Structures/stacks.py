class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as parametr and appends it to the end of the list.
        returns nothing.
        The runtime for this method is O(1), or constant time, becasue appending 
        to the end of the list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """
        This method removes and returns the last item from the list, which also the
        top item of the stack.

        The runtime here is constant time, because all it does is index to the last 
        item of the list.
        """
        return self.items.pop()

    def peek(self, item):
        """
        This method returns the lst item in the list, which is also the item 
        at the top of the stack

        """
        if self.items:
            return self.items[-1]
        return None

    def size(self,item):

        """
        This method returns lenght of the list that is representing the Stack.
        This method  runs in constant time because finding the lenght of the list
        also in constant time
        """
        return len(self.items)
    
    def is_empty(self,item):
        """
        This method return returns a Booleam value describing whethe or not the stack is empty
        This method runs in constant time
        """
        return self.items == []
