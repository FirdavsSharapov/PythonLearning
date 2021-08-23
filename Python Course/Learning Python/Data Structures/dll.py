# Doubly Linked List
class DoublyLinkedList:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        

    def __repr__(self):
        return "SLLNode object: data = {}".format(self.data)

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """replace the xisting value of the self.data attribute with new_data"""
        self.data = new_data

    def get_next(self):
        """Return the self.data attribute"""
        self.next

    def set_next(self, new_next):
        """replace the existing value of the self.next attribute with new_data"""
        self.next = new_next

    def get_prev(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_prev(self,new_previous):
        """replace the existing value of the self.new_previous attribute with new_data"""
        self.next = new_previous
