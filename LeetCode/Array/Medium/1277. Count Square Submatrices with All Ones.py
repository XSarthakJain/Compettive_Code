#1277. Count Square Submatrices with All Ones
#Medium
matrix = [
  [0,0,0],[0,1,0],[0,1,0],[1,1,1],[1,1,0]
]

for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        if matrix[i-1][j]>0 and matrix[i][j-1]>0 and matrix[i-1][j-1]>0 and matrix[i][j]>0:
            matrix[i][j]=matrix[i][j]+min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
c=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]>0:
            c+=matrix[i][j]
print(c)
        
        
