#876. Middle of the Linked List
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
    def middleElement(self):
        slowPointer = self.head
        fastPointer = self.head
        while(fastPointer and fastPointer.next is not None):
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        else:
            return slowPointer
        
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
obj2 = LinkedList()
print("Middle Element LinkedList = ")
obj2.head = obj.middleElement()
obj2.display()

        
