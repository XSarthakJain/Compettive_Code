#118. Pascal's Triangle
numRows = 5
resultSet = [[1]]
for i in range(2,numRows+1):
    temp = []
    for item in range(i):
        if item==0 or item==i-1:
            temp.append(1)
        else:
            temp.append(resultSet[-1][item-1]+resultSet[-1][item])
    resultSet.append(temp)
print("Result = ",resultSet)
    
