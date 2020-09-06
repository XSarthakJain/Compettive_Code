#Check Palindrome
class LinkedList:
    def __init__(self):
        self.head=None

    def PrintData(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def Palindrome(self):
        temp=self.head
        p1=temp
        flag=True

        if temp==None:
            print("Linked List is Empty")
            return
        elif temp.next==None or temp.next.next==None:
            if (temp.next!=None) and (temp.data!=temp.next.data):
                flag=False
        else:
                
            while(p1):

                if p1.next!=None:
                    p1=p1.next.next
                    temp=temp.next

                else:
                    
                    break
            prev=None
            while(temp):
                next=temp.next
                temp.next=prev
                prev=temp
                temp=next
            
                
            temp=self.head
            while(temp!=None or prev!=None):
                
                if prev.data!=temp.data:
                    
                    flag=False
                    break

                prev=prev.next
                temp=temp.next
        if flag:
            print("Linked List is Palindrome")
                
        else:
            print("Linked List is not Palindrome")
            
                
            


        
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

if __name__=="__main__":

    l1=LinkedList()
    #l1.head=Node(5)
    #l2=Node(10)
    #l3=Node(5)
    #l4=Node(10)
    #l5=Node(5)
    #l1.head.next=l2
    #l2.next=l3
    #l3.next=l4
    #l4.next=l5
    l1.PrintData()
    l1.Palindrome()
