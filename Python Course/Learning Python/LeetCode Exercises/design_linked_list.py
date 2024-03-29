class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for i in range(0, index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:    
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        current = self.head
        newNode = ListNode(val)

        if index <= 0:
            newNode.next = current
        else:
            for i in range(index - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode
        
        self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                current = current.next
            current.next = current.next.next              

        self.size -= 1


if __name__ == '__main__':
    newLinked = MyLinkedList()
    newLinked.addAtHead(2)

    print(newLinked.get(0))