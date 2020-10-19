#Reverse The Array
A=list(map(int,input().split()))
for i in range(len(A)//2):
    A[i],A[(len(A)-1-i)]=A[(len(A)-1-i)],A[i]
print(*A)
