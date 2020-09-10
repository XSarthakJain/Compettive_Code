#Check Paranthesis

def ParanthesisCheck(exp):
    stack=[]
    for char in exp:
        if char in ['{','[','(']:
            stack.append(char)
        else:
            if not stack:
                return False
            current=stack.pop()

            if current=="{":
                if char!="}":
                    print("Zero")
                    return False

            elif current=="[":
                if char!="]":
                    print("One")
                    return False

            elif current=="(":
                if char!=")":
                    print("Two")
                    return False

    if stack:
        return False
    return True


if ParanthesisCheck("[{}]"):
    print("Balanced Paranthesis")
else:
    print("Unbalanced Paranthesis")
                
            
