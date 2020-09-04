#Nth Node from the end of the Linked List

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

    def Nth_Node(self,n):
        temp=self.head
        counter=0
        while(temp):
            counter+=1
            temp=temp.next
        counter=counter-n+1
        counter1=0
        temp=self.head
        while(temp):
            counter1+=1
            if counter==counter1:
                print("Nth Node = ",temp.data)
                break
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

    l1.PrintData()

    l1.Nth_Node(5)
