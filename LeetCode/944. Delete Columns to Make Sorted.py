#944. Delete Columns to Make Sorted
strs =  ["cba","daf","ghi"]
result = 0
for i in range(len(strs[0])):
    prev = strs[0][i]
    for j in range(len(strs)):
        if strs[j][i] < prev:
            result+=1
            break
        prev = strs[j][i]
print(result)
'''
for i in range(len(strs[0])):
    temp = []
    for j in range(len(strs)):
        temp.append(strs[j][i])
    if temp != sorted(temp):
        result+=1
print("Result = ",result)
'''
