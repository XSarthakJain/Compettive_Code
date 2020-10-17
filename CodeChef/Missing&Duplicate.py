A=list(map(int,input().split()))
for i in range(len(A)):
    
    if A[i]!=i:
        #print(A)
        A[A[i]],A[i]=A[i],A[A[i]]
print(A)
