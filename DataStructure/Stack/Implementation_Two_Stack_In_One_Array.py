#Implementation Two Stack in an Array
from collections import defaultdict

def CreateStack():
    stack=[0]*100
      
   
    return stack

def Push(stack,data,top):
    print("top value from PUSH",(top))
    stack.insert(top,data)
    return stack,(top+2)

def Pop(stack):
    stack.pop()
    return stack
def Peek(stack):
    return stack[-1]
def IsEmpty(stack):
    if len(stack)<1:
        return True
    else:
        return False
def Print(stack,top):
    print("Stack Display = ",top)
    print(stack)
    
    for i in range(top,-1,-2):
        
        print(stack[i])
    return 


top1=0
top2=1
stack=CreateStack()
stack,top1=Push(stack,5,top1)#For Stack1
#print("Top 1 =",top1)
stack,top1=Push(stack,6,top1)#For Stack1
#print("Top 1 =",top1)
'''stack,top1=Push(stack,7,top1)#For Stack1
stack,top1=Push(stack,8,top1)#For Stack1
stack,top1=Push(stack,9,top1)#For Stack1

'''

stack,top2=Push(stack,15,top2)#For Stack2
'''
stack,top2=Push(stack,15,top2)#For Stack2
stack,top2=Push(stack,15,top2)#For Stack2
stack,top2=Push(stack,15,top2)#For Stack2

'''
Print(stack,top1)#For Stack1




