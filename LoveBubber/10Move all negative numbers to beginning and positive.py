#Move all negative numbers to beginning and positive to end with constant extra space
A=list(map(int,input().split()))
j=0
for i in range(len(A)):
    if A[i]<0:
        A[i],A[j]=A[j],A[i]
        j+=1
print(A)
