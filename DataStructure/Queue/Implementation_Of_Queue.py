#Implementation Of Queue
class Queue:
    def __init__(self,c):
        self.queue=[]
        self.rear=0
        self.front=0
        self.capacity=c

    def Enqueue(self,data):
        if self.capacity==self.rear:
            print("Queue is Full")
        else:
            self.queue.append(data)
            self.rear+=1
    def Dequeue(self):
        if self.rear==self.front:
            print("List has no Item")
        else:
            self.queue.pop(0)
            self.rear-=1
    def Front(self):
        if self.front==self.rear:
            print("List is Empty")
        else:
            print("Self Front = ",self.queue[self.front])
    def Display(self):
        for i in range(self.rear):
            print(self.queue[i])


if __name__=="__main__":
    q1=Queue(10)
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
            
