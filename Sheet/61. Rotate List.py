#61. Rotate List
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
    def rotate(self,k):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp = temp.next
        if count==0:
            return self.head
        k = k%count
        temp = self.head
        while(k>0 and temp is not None and temp.next is not None):
            while(temp.next and temp.next.next is not None):
                temp = temp.next
            node = temp.next
            temp.next = None
            node.next = self.head
            self.head = node
            k-=1
            temp = self.head
        return self.head
            
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(2)
obj.push(1)
obj.head = obj.rotate(2)
obj.display()

