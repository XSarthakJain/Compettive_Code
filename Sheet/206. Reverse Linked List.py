#206. Reverse Linked List
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
    def reverseLL(self):
        def reverseinside(current):
            prev = None
            if current is None:
                self.head = prev
                return
            next_val = current.next
            current.next = prev
            prev = current
            current = next_val
            return reverseinside(current)
        reverseinside(self.head)
        
        
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

obj = LinkedList()
obj.push(5)
obj.push(15)
obj.push(25)
obj.push(35)
obj.push(45)
obj.push(55)
obj.display()
obj.reverseLL()
print("After Reverse = ",)
obj.display()

    

