#237. Delete Node in a Linked List
#Delete Node in O(1) Time Complexity
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
    def deleteNode(self,node):
        node.data = node.next.data
        node.next = node.next.next
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(5)
obj.push(15)
obj.push(25)
obj.push(30)
obj.push(100)
obj.deleteNode(obj.head.next)
obj.display()
        
