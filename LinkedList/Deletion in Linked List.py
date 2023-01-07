#Deletion in Linked List from Beginning
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next
    def deleteBeg(self):
        self.head = self.head.next
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(5)
obj.push(10)
obj.push(15)
obj.push(20)
obj.push(25)
obj.display()
obj.deleteBeg()
print("After Deletion = ")
obj.display()
