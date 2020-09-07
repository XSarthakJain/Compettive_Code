#Implementation of Stack
#Main Functionality of Stack is Push(),Pop(),Peek(),isEmpty()



def createStack():
    stack=[]
    return stack

def Push(stack,data):
    stack.append(data)
    return stack

def Pop(stack):
    if len(stack)<1:
        print("Underflow Stack")
        return
    print("Poped Element = ",stack[-1])
    stack.pop()
    return stack

def Peek(stack):
    for i in stack:
        print("Stack Element = ",i)
    return

def isEmpty(stack):
    if len(stack)<1:
        print("Stack is Empty")
    else:
        print("Stack has an Element")
    return

if __name__=="__main__":
    
    
    stack=createStack()
    Push(stack,5)
    Push(stack,15)
    Push(stack,25)
    Push(stack,35)
    Peek(stack)
    Pop(stack)
    Peek(stack)
    
