#Minimise the Maximum Difference between Height
A=list(map(int,input().split()))
K=int(input())
if len(A)==0:
    print("0")
else:
    minimum=min(A)
    for i in range(len(A)):
        if A[i]==minimum:
            A[i]+=K
        else:
            A[i]-=K
    print((max(A))-(min(A)))
