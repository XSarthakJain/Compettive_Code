#Common elements in all rows of a given matrix
n=int(input())
A=[]
for i in range(n):
    temp=[]
    temp=list(map(int,input().split()))
    A.append(temp)

#Operation
if n>1:
    s1=set()
    s1=set(A[0]).intersection(set(A[1]))

    for i in range(2,n):
        s1=s1.intersection(set(A[i]))

    print(*s1)
else:
    print(*A)
