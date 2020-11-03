#Kth element in Matrix
n=int(input())
mat=[]
for i in range(n):
    temp=[]
    temp=list(map(int,input().split()))
    mat.append(temp)
k=int(input())
#Operation

help_list=[]
for i in range(n):
    for j in range(n):
        help_list.append(mat[i][j])
help_list.sort()

print(help_list[k-1])
