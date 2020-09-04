#Middle Node of a Linked List
class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def MiddleNode(self):
        temp=self.head

        if temp==None:
            return
        elif temp.next==None or temp.next.next==None:
            print("Middle Node = ",temp.data)
            return
        ptr1=self.head
        while(temp):
            print("temp,ptr1",temp.data,ptr1.data)
            if  ptr1.next==None or ptr1.next.next==None:
                print("Middle Node = ",temp.data)
                break

            
            if ptr1.next!=None:
                ptr1=ptr1.next.next
            temp=temp.next
            
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

   

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

    l1.PrintData()
    l1.MiddleNode()
