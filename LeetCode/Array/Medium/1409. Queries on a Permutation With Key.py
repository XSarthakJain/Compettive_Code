queries=[3,1,2,1]
operation=[]
result=[]
m=5
for i in range(1,m+1):
    operation.append(i)
print("operation",operation)
for j in queries:
    result.append(operation.index(j))
    operation.remove(j)
    operation.insert(0,j)
print(result)
