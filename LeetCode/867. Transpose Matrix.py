#867. Transpose Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = []
for i in range(len(matrix[0])):
    temp = []
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    result.append(temp)
print("Result =",result)
