#944. Delete Columns to Make Sorted
strs =  ["cba","daf","ghi"]
result = 0
for i in range(len(strs[0])):
    temp = []
    for j in range(len(strs)):
        temp.append(strs[j][i])
    if temp != sorted(temp):
        result+=1
print("Result = ",result)
