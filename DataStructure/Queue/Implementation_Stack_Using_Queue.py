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
           self.queue.pop(0)
           rear-=1

            
            
    def Front(self):
        if self.rear==self.front:
            print("Queue is Empty")
        else:
            print("Queue Front Element = ",self.queue[self.front])
    def Display(self):
        for i in range(self.rear):
            print("Queue Element = ",self.queue[i])
        return

if __name__=="__main__":
    q1=Queue(5)
    q2=Queue(10)
    q1.Enqueue(5)
    q1.Enqueue(15)
    q1.Enqueue(25)
    q1.Enqueue(15) 
    q1.Enqueue(55)

    q1.Display()
    q1.Dequeue()
    
        
    q1.Display()
    print("Front")
    q1.Front()
            
