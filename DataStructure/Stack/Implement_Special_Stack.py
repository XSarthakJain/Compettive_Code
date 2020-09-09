#Design and Implement Special Stack
'''Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure and no other data structure like arrays, list, .. etc.'''

def CreateStack():
    stack=[]
    stack1=[]
    return stack,stack1

def Push(stack,stack1,data):
    if isEmpty(stack):
        stack1.append(data)
        stack.append(data)
    else:
        if data<stack[-1]:
            stack1=Pop(stack1)
            stack1.append(data)
        
        stack.append(data)
    
    return stack,stack1
def Pop(stack):
    if isEmpty(stack):
        print("Underflow")
        return
    else:
       
        print("Poped Element = ",stack[-1])
        stack.pop()
        return stack
def Peek(stack):
    for i in Peek:
        print("Stack Items = ",Peek)
    return
def isEmpty(stack):
    if len(stack)<1:
        print("No Element")
        return True
    else:
        print("Present Element")
        return False
def StackMin(stack1):
    print("Minimum Element is = ",stack1[-1])
    return
Stack,Stack1=CreateStack()
Stack,Stack1=Push(Stack,Stack1,5)
Stack,Stack1=Push(Stack,Stack1,15)
Stack,Stack1=Push(Stack,Stack1,25)
Stack,Stack1=Push(Stack,Stack1,3)
Stack,Stack1=Push(Stack,Stack1,45)
Stack,Stack1=Push(Stack,Stack1,55)

'''Stack=Pop(Stack)
Stack=Pop(Stack)
Stack=Pop(Stack)
Stack=Pop(Stack)
'''
StackMin(Stack1)
