#1222. Queens That Can Attack the King
queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
king = [3,3]
result=[]
a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    print(temp)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    a=a-1
    b=b-1

a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    a=a+1
    b=b+1

a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    a=a-1
    b=b+1

a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    a=a+1
    b=b-1


a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    a=a+1
a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    a=a-1
a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    b=b+1
a=king[0]
b=king[1]
while(True):
    
    temp=[]
    temp.append(a)
    temp.append(b)
    if temp in queens:
        result.append(temp)
        break
    elif temp[0]>7 or temp[1]>7 or temp[0]<0 or temp[1]<0:
        break
    b=b-1
print(result)






