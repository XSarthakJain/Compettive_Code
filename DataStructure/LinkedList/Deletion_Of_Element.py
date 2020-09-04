class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def Deletion(self,n):
        print("Deletion == ",n)
        
        if self.head.data==n:
            print("Done")
            self.head=self.head.next
        temp=self.head
        add_P=self.head
        while(temp):
            if temp.data==n:
                add_P.next=temp.next
                
            add_P=temp
            temp=temp.next
            
                
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l3=Node(20)
    l4=Node(30)
    l5=Node(10)
    l6=Node(5)
    l7=Node(60)


    l1.head.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    l5.next=l6
    l6.next=l7
    l1.PrintData()
    l1.Deletion(5)
    l1.PrintData()
