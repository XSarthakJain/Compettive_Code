#Reverse the Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
    def ReverseLinkedList(self):
        current=self.head
        prev=None
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

          
            

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l3=Node(20)
    l4=Node(30)
    l5=Node(40)
    l1.head.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5

    l1.PrintData()
    l1.ReverseLinkedList()
    l1.PrintData()
