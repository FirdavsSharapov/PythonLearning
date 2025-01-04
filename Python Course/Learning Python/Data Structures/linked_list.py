class ListNode:
    def __init__(self, val=0) -> None:
        self.val = val # The value (data stored in the node)
        self.next = None #Points to the next node (initially none)\
    

    
    

def print_linked_list(head):
    if not head:
        print("Empty list")
        return
    current = head # Start from the head node
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print('None') 


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

print_linked_list(node3)