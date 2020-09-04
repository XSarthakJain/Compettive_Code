#Deleting Element by Index

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self,):
        self.head=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def DeletingElementByIndex(self,ind):
        temp=self.head
        i=0
        temp1=temp
        if temp!=None:
            if ind==0:
                self.head=self.head.next
                return
            while(temp):
                if i==ind:
                    temp1.next=temp.next
                    break
                i+=1
                temp1=temp
                temp=temp.next
                
        

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l1.head.next=l2

    l1.PrintData()

    l1.DeletingElementByIndex(0)
    l1.PrintData()
