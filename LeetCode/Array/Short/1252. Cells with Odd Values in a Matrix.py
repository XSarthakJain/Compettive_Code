#1252. Cells with Odd Values in a Matrix

n = 2
m = 2
indices = [[1,1],[0,0]]
#array=[[0]*m]*n
array=[]


for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(0)
    array.append(temp)
        
for i in indices:
    row_item=i[0]
    col_item=i[1]
    
    for col in range(m):
        array[row_item][col]+=1

    for row in range(n):
        array[row][col_item]+=1

   
result=0
for i in range(n):
    for j in range(m):
        if array[i][j] & 1:
            result+=1
print(result)
