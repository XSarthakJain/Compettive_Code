#Given a collection of intervals, merge all overlapping intervals.
n=int(input())
A=[]
for i in range(n):
    temp=list(map(int,input().split()))
    A.append(temp)

A.sort(key=lambda x:x[0])

result=[]
temp=A[0]
i=1
l=len(A)
while(i<l):
    print(temp,A[i])
    if temp[0]==(A[i][0]-1):
        temp1=[]
        temp1.append(temp[0])
        temp1.append(max(temp[1],A[i][1]))
        temp=temp1
        i+=1
    else:
        result.append(temp)
        temp=A[i]
        i+=1
result.append(temp)
print(result)
