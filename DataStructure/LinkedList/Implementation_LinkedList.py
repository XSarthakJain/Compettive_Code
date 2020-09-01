#Implement of LinkedList
class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
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
    l4=Node(25)

    l1.head.next=l2
    l2.next=l3
    l3.next=l4

    l1.PrintData()
