#Sort an array of 0s, 1s and 2s
A=list(map(int,input().split()))
zero=0
one=0
for i in A:
    if i==0:
        zero+=1
    elif i==1:
        one+=1
result=[]
result.extend("0"*zero)
result.extend("1"*one)
result.extend("2"*(len(A)-(zero+one)))
print(*result)
        
