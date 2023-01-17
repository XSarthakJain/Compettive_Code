#Reverse Linked List in groups of Size K
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
def reverseLL(head,k):
    if head == None:
        return None
    current = head
    count = k
    while(count>0):
        if current is None:
            return head
        current =  current.next
        count-=1
    node_next = None
    prev = None
    current = head
    count = k
    while count>0 and current:
        node_next = current.next
        current.next = prev
        prev = current
        current = node_next
        count-=1
    if count!=0:
        return head
    if node_next!=None:
        head.next = reverseLL(node_next,k)
    return prev
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj  = LinkedList()
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(2)
obj.push(1)


obj.display()
print("Reverse LinkedList = ")
k = 3
l2 = LinkedList()
l2.head = reverseLL(obj.head,k)
l2.display()
