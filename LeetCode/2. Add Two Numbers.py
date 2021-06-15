#2. Add Two Numbers
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def PrintData(self):
        Linkedlist = self.head
        
        while(Linkedlist):
            print(Linkedlist.data)
            Linkedlist = Linkedlist.next

    def Push(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = newNode
        

def addTwoNumber(l1,l2):
    third = LinkedList()
    carry = 0
    data =0
    while(l1 is not None and l2 is not None):
        temp = l1.data + l2.data + carry
        if temp-9 > 0:
            data = temp%10
            carry = temp//10
        else:
            data = temp
            carry = 0
        third.Push(data)
        l1 = l1.next
        l2 = l2.next
    print("carry",carry)
    if l1 is not None:
        while(l1):
            temp = l1.data+carry
            print("temp",temp)
            if temp-9 > 0:
                data = temp%10
                carry = temp//10
            else:
                data = temp
                carry = 0
            third.Push(data)
            l1 = l1.next

    if l2 is not None:
        while(l2.next):
            temp = l2.data+carry
            if temp-9 > 0:
                data = temp%10
                carry = temp//10
            else:
                data = temp
                carry = 0
            third.Push(data)
            l2 = l2.next
    if carry != 0:
        third.Push(carry)
            
    third.PrintData()


if __name__ == "__main__":
    l1 = LinkedList()
    l1.Push(9)
    l1.Push(9)
    l1.Push(9)
    l1.Push(9)
    l1.Push(9)
    l1.Push(9)
    l1.Push(9)
    
       
    #l1.PrintData()

    l2 = LinkedList()
    l2.Push(9)
    l2.Push(9)
    l2.Push(9)
    l2.Push(9)
   
    
    
    addTwoNumber(l1.head,l2.head)
    
