class SLLNode:

    def __init__(self,data):
        self.data = data
        self.next = None
    
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


class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object: head={}".format(self.head)
    
    def is_empty(self):
        pass

    def add_front(self, nex_data):
        pass

    def size(self):
        pass

    