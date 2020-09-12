#Double Ended Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
        
    def Enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last.next.prev=self.last
            self.last=self.last.next
    def Dequeue(self):
        if self.head is None:
            return None
        else:
            temp=self.head.next
            self.head=self.head.next
            self.head.prev=None
            return temp
    def first(self):
        return self.head.data
    def size(self):
        temp=self.head
        size=0
        while(temp):
            size+=1
            temp=temp.next
        return size
    def isEmpty(self):
        if self.last is None:
            return True
        else:
            return False
    def PrintQueue(self):
        temp=self.head
        while(temp):
            print(temp.data,end=",")
            temp=temp.next
        print("")
        return

if __name__=="__main__":

    q1=Queue()
    q1.Enqueue(5)
    q1.Enqueue(10)
    q1.Enqueue(15)
    q1.Enqueue(20)
    q1.PrintQueue()
    q1.Dequeue()
    q1.PrintQueue()
        
    
        
