#Reverse a linked list by Iterative Method
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def display(self):
        temp = self.head
        print("LinkedList = ")
        while(temp!=None):
            print(temp.data, end='  ')
            temp = temp.next
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(5)
obj.push(10)
obj.push(15)
obj.push(20)
obj.display()
obj.reverse()
obj.display()
