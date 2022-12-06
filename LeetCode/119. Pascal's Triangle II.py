#119. Pascal's Triangle II
rowIndex = 3
resultSet = [[1]]
for i in range(rowIndex+1):
    temp = []
    for item in range(i+1):
        if item == 0 or item==i:
            temp.append(1)
        else:
            temp.append(resultSet[-1][item-1]+resultSet[-1][item])
    resultSet.append(temp)
print(resultSet)
