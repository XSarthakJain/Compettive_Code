#Implementation of Circular Linked List
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
            if temp.next==self.head:
                print(temp.data)
                break
            else:
                print(temp.data)
                temp=temp.next
    def DeleteLinkedList(self,n):
        temp=self.head
        if temp==None:
            return
        p1=temp
        while(temp):
            if temp.data==n:
                p1.next=temp.next
                break
                
            else:
                p1=temp
                temp=temp.next
                
    def Push(self,n):
        temp=self.head
        if temp==None:
            temp.self=Node(n)
            temp.next=self.head
        else:
            temp=temp.next
            while(temp):
                print("Value = ",temp.next,temp)
                if temp.next==self.head:
                    temp.next=Node(n)
                    return
                temp=temp.next
                
                
        
                
            
            
        

if __name__=="__main__":

    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l3=Node(15)
    l4=Node(20)
    l5=Node(25)

    l1.head.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    
    l5.next=l1.head
    l1.Push(100)
    l1.DeleteLinkedList(15)
    l1.PrintData()


