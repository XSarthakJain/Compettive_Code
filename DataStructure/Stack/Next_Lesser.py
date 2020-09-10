#Next Greater Element 

class Stack:
    def __init__(self):
        self.stack=[]
    def Push(self,data):
        self.stack.append(data) 
    def Pop(self):
        return  self.stack.pop()

    def Isempty(self):
        return len(self.stack)==0
    def Top(self):
        return self.stack[-1]
    

    
    
if __name__=="__main__":
    s1=Stack()
    n=list(map(int,input().split()))

    for i in n:
        if s1.Isempty():
            s1.Push(i)
        else:
            while( not s1.Isempty() and s1.Top()>i):
                print("the next Greater Element is ",s1.Pop(),i)
                
                
            s1.Push(i)

    while s1.stack:
        print("the next Greater Element is ",s1.Pop(),"-1")
        
        
            
    
    
