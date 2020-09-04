#Count Node Occurances
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

    def Count_Occurance(self):
        d=dict()
        temp=self.head
        while(temp):
            if temp.data in d:
                d[temp.data]=d[temp.data]+1
            else:
                d[temp.data]=1
            temp=temp.next

        for i in d:
            print(f"Occurances Of {i} {d[i]}")

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l3=Node(15)
    l4=Node(20)
    l5=Node(25)
    l6=Node(15)
    l1.head.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    l5.next=l6

    l1.PrintData()
    l1.Count_Occurance()
