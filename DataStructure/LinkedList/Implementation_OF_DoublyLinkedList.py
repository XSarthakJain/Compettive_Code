#Implementation of Doubly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        temp=self.head
        print("Forward Print")
        while(True):
            print(temp.data)
            if temp.next!=None:
                temp=temp.next
            else:
                break
                
            
        print("Backword Print")
        
        while(temp):
            
            print(temp.data)
            temp=temp.prev

    def Push(self,data):
        temp=self.head
        if temp==None:
            self.head=Node(data)
        else:
            while(temp.next!=None):
                temp=temp.next

            temp.next=Node(data)
            temp.next.prev=temp
            
    def Delete(self,data):
        temp=self.head
        p1=temp
        while(temp):
            if temp.data == data:
                print("Values ",temp.data,p1.data)
                p1.next=temp.next
                if temp.next!=None:
                    temp.next.prev=temp.prev
                
                break
                
            p1=temp
            temp=temp.next

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

    l2.prev=l1.head
    l3.prev=l2
    l4.prev=l3
    l5.prev=l4

    l1.PrintData()

    l1.Push(80)

    l1.PrintData()

    l1.Delete(80)
    l1.PrintData()
                
