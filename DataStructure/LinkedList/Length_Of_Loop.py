#Find Length of Loop

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
    def Count_Loop(self):
        temp=self.head
        if temp==None:
            return
        else:
            ptr=temp
            i=0
            
            while(temp): 
                if temp.next==ptr.next and i!=0:

                    if ptr.next==ptr.next.next:
                        print("Loop = 1")
                    else:
                        print("Loop = ",i)
                    break
                i+=1
            
                if ptr.next!=None:
                    temp=temp.next
                    ptr=ptr.next.next
                else:
                    break
                    
            

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    #l1.head.next=l1.head
    l2=Node(10)
    l3=Node(10)
    l4=Node(10)
    l5=Node(10)

    l1.head.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    l5.next=l2
    #l1.PrintData()
    l1.Count_Loop()
