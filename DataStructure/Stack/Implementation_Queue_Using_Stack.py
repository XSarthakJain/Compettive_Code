#Implementation Queue Using Stack
class Stack:
    def __init__(self):
        self.stack=[]
        self.top=0

    def Push(self,data):
        self.stack.append(data)
        self.top+=1

    def Pop(self):
        temp=self.stack[-1]
        self.stack.pop()
        self.top-=1
        return temp
    def display(self):
        for i in range(self.top):
            print("Stack Element = ",self.stack[i])

class Queue:
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()
        self.size=0
    def Enqueue(self,data):
        self.s1.Push(data)
        self.size+=1
    def Dequeue(self):

        for i in range(self.size):
            self.s2.Push(self.s1.Pop())

        self.s2.Pop()
        self.size-=1
        for i in range(self.size):
            self.s1.Push(self.s2.Pop())


    def Display(self):
        self.s1.display()
        
if __name__=="__main__":
    
    q1=Queue()
    q1.Enqueue(5)
    q1.Enqueue(15)
    q1.Enqueue(25)
    q1.Enqueue(35)
    q1.Enqueue(45)

    q1.Display()
    q1.Dequeue()
    q1.Dequeue()

    q1.Display()
    '''
    s1=Stack()
    s1.Push(5)
    s1.Push(15)
    s1.Push(25)
    s1.Push(35)
    s1.Push(45)
    s1.display()
    s1.Pop()
    s1.display()
'''
