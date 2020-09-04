#Delete the number of before given value
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

    def Delete_Before(self,n):

        #Delete
        print("Deletion ==",n)
        temp=self.head
        temp1=self.head
        if self.head==None:
            return
        elif self.head.data==n:
            return
        elif temp.next.data==n:
            
            self.head=self.head.next
            
        else:
            while(temp.next!=None):
                
                if temp.next.data==n:
                    
                    temp1.next=temp.next
                    break
                temp1=temp
                temp=temp.next
                
                
        
        
            

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(5)
    l2=Node(10)
    l3=Node(15)

    l1.head.next=l2
    l2.next=l3
    

    l1.PrintData()

    #############
    l1.Delete_Before(511)
    l1.PrintData()

    
