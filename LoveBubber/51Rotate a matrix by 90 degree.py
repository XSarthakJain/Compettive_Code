#Rotate a matrix by 90 degree in clockwise direction without using any extra space
#Input here
N=int(input())
A=[]
for i in range(N):
    temp=[]
    temp=list(map(int,input().split()))
    A.append(temp)

#Operation Task1

for i in range(N):
    for j in range(i,N):
        A[i][j],A[j][i]=A[j][i],A[i][j]


#Reverse Each row
for i in range(N):
    A[i].reverse()
print(A)
