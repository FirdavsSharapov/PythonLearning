class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        newNode = ListNode(value)
        if self.head == None:
            self.head = newNode
        else:
            self.head.next = newNode

        self.size += 1

    def prepand(self, value):
        newNode = ListNode(value)
        if self.head == None:
            self.head = newNode
        else:
            current_node = self.head
            self.head = newNode
            self.head.next = current_node

        self.size += 1


myLinkedList = LinkedList()
myLinkedList.prepand(3)
myLinkedList.prepand(4)
myLinkedList.prepand(5)

print(myLinkedList)





