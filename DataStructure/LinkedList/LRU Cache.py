#LRU Cache
class Node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
        

class LinkedList:
    def __init__(self):
        self.head=None
        self.limit=3
        self.current=0

   
    def Delete(self):
        temp=self.head
        self.head=self.head.next
        self.head.next.prev=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print("LRU = ",temp.data)
            temp=temp.next

if __name__=="__main__":
    n1=LinkedList()
    n1.head=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(1)
    n6=Node(2)
    n7=Node(5)
    n8=Node(1)
    n9=Node(2)
    n10=Node(3)
    n11=Node(4)
    n12=Node(5)

    n1.head.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n5.next=n6
    n6.next=n7
    n7.next=n8
    n8.next=n9
    n9.next=n10
    n10.next=n11
    n11.next=n12
    
    n12.prev=n11
    n11.prev=n10
    n10.prev=n9
    n9.prev=n8
    n8.prev=n7
    n7.prev=n6
    n6.prev=n5
    n5.prev=n4
    n4.prev=n3
    n3.prev=n2
    n2.prev=n1


    n1.PrintData()
