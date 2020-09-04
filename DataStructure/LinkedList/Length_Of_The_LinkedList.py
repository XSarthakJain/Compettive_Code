#Find a Length of LinkedList Iterative and Recursive

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def Iterative_Length(self):
        temp=self.head
        length=0
        while(temp):
            length+=1
            temp=temp.next
        print("Length of the LinkedList = ",length)

    def Recursive_Length(self):
        pass
        

if __name__=="__main__":
    l1=Linkedlist()
    l1.head=Node(5)
    l2=Node(10)
    l1.head.next=l2
    l1.PrintData()
    l1.Iterative_Length()
