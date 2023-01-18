#234. Palindrome Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
def palindrome(head):
    if head is None:
        return false
    count = 1
    slow = fast = head
    while(fast.next and fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next
    first = head
    prev = None
    current = slow.next
    while(current):
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    while(prev):
        if prev.data != first.data:
            return False
        prev = prev.next
        first = first.next
    return True
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

obj = LinkedList()
obj.push(10)
obj.push(2)
obj.push(3)
obj.push(2)
obj.push(1)

print(palindrome(obj.head))
