#Set Matrix Zero
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

#Approach 1
row = 1
col = 1
for r in range(len(matrix)):
    if matrix[0][r] == 0:
        col = 0
        break
for c in range(len(matrix[0])):
    if matrix[c][0] == 0:
        row = 0
        break

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
            matrix[0][c] = 0
            matrix[r][0] = 0
for r in range(1,len(matrix)):
    for c in range(1,len(matrix[0])):
        if matrix[0][c] == 0:
            matrix[r][c] = 0
        elif matrix[r][0] == 0:
            matrix[r][c] = 0
for r in range(len(matrix)):
    if row == 0:
        matrix[r][0] = 0
for c in range(len(matrix[0])):
    if col == 0:
        matrix[0][c] = 0
print("Result  = ",matrix)

#Approach 2            
'''
row = [1]*len(matrix)
col = [1]*len(matrix[0])

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
            row[r] = 0
            col[c] = 0
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if row[r]==0:
            matrix[r][c] = 0
        elif col[c] == 0:
            matrix[r][c] = 0
print("Result = ",matrix)
'''

#Approach 3
'''
result = []
for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix[0])):
        temp.append(matrix[i][j])
    result.append(temp)

for i in range(len(matrix)):
    flag = False
    temp = []
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            if i!=0:
                for k in range(i,-1,-1):
                    result[k][j] = 0
            flag = True
        else:
            if i!=0 and matrix[i-1][j] == 0:
                matrix[i][j] = 0
                temp.append(0)
            else:
                temp.append(matrix[i][j])
    if flag:
        result[i] = [0]*len(matrix[0])
    else:
        #print(temp,i)
        result[i] = temp
print(result)
'''
                
            
    
