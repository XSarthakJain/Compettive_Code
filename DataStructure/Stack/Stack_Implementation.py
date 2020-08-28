#Implementation Of Stack


def CreateStack():
    stack=[]
    return stack

def push(stack,item):
    stack.append(item)
    #top+=1
    print("Pushed Item = ",item)

def pop(stack):

    #Check Empty
    temp1=isEmpty(stack)
    if temp1:
        print("UnderFlow Error")
    else:
        return stack.pop()

def isEmpty(stack):
    if len(stack)<1:
        return True
    else:
        return False
def peek(stack):
    if isEmpty(stack):
        return("UnderFlow Error")
    else:
        return stack[-1]

stack=CreateStack()
push(stack,5)
push(stack,15)
push(stack,25)
push(stack,125)
push(stack,625)
print("Poped Item = ",pop(stack))
print(peek(stack))


