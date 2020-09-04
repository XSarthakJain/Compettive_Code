#Find Loop
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


    def CheckLoop(self):
        temp=self.head
        flag=True
        if temp==None:
            return
        elif temp.next==None or temp.next.next==None:
            pass
        
        else:
            ptr1=temp
            i=0
            
            while(temp):
                #print("temp.data,ptr1.data",temp.data,ptr1.data)
                if temp.next==ptr1.next and i!=0:
                    print("Loop Exist")
                    flag=False
                    break
                i+=1

                if ptr1.next!=None:
                    ptr1=ptr1.next.next
                    temp=temp.next
                else:
                    
                    break
                    
        if flag:
            print("Loop does not Exist")
            return
                

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l1.head.next=l2
    #l5.next=l3

    #l1.PrintData()

    l1.CheckLoop()


    
