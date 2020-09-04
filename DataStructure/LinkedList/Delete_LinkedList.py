#Delete LinkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def PrintData(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l1.head.next=l2
    l1.PrintData()
    del(l1)
    l1.PrintData()
