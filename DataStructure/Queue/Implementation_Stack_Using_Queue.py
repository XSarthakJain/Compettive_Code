#Create Stack Using Queue
class Queue:
    def __init__(self,c):
        self.queue=[]
        self.rear=0
        self.front=0
        self.capacity=c
    def Enqueue(self,data):
        if self.rear==self.capacity:
            print("Queue is Overflow")
            return
        self.queue.append(data)
        self.rear+=1

    def Dequeue(self):
        if self.front==self.rear:
            print("Queue is Underflow")
        else:
            temp=self.queue[0]
            self.queue.pop(0)
            self.rear-=1
            return temp

            
            
    def Front(self):
        if self.rear==self.front:
            print("Queue is Empty")
        else:
            print("Queue Front Element = ",self.queue[self.front])
    def Display(self):
        for i in range(self.rear):
            print("Queue Element = ",self.queue[i])
        return


class stack:
    def __init__(self):
        self.q1=Queue(10)
        self.q2=Queue(10)
        self.size=0
    def Push(self,data):
        self.q1.Enqueue(data)
        self.size+=1
    def Pop(self):
        
        for i in range(self.size-1):
            temp=self.q1.Dequeue()
            self.q2.Enqueue(temp)
        temp=self.q1.Dequeue()

        for i in range(self.size-1):
            temp=self.q2.Dequeue()
            self.q1.Enqueue(temp)

        self.size-=1
    def display(self):
        self.q1.Display()
        return
            
        
            
        

if __name__=="__main__":
    s1=stack()
    s1.Push(5)
    s1.Push(15)
    s1.Push(25)
    s1.Push(35)
    s1.Push(45)
    s1.Pop()
    s1.Push(55)
    s1.display()
            
