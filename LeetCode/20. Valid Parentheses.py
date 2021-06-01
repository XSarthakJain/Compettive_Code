#20. Valid Parentheses
s = input()
flag = False
result = []
for i in s:
    if i == "(" or i == "{" or i=="[":
        result.append(i)
    else:
        if(len(result)<1):
            result.append(i)
            flag = False
            break
        else:
            if i==")" and result[-1] == "(":
                del result[-1]
                flag = True
            elif i=="}" and result[-1] == "{":
                del result[-1]
                flag = True
            elif i=="]" and result[-1] == "[":
                del result[-1]
                flag = True
            else:
                flag = False
                result.append(i)
                break
print(False if (len(result)!=0) else True)
