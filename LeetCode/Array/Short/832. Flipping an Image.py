#832. Flipping an Image
A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
for i in range(len(A)):
    A[i]=A[i][::-1]
#for Invert
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==0:
            A[i][j]=1
        else:
            A[i][j]=0
print(A)
