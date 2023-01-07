#Insert a node after a given node
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,prevNode,newNode):
        #Create New Node
        new_Node = Node(newNode)
        temp = self.head
        if self.head == None:
            self.head = new_Node
            return
        while(temp!=None):
            if temp.data == prevNode:
                new_Node.next = temp.next
                temp.next = new_Node
                break
            elif temp.next == None:
                temp.next = new_Node
                break
            temp = temp.next
    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next
            
            

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
obj = LinkedList()
obj.push(1,5)
obj.push(12,10)
obj.push(5,15)
obj.display()

