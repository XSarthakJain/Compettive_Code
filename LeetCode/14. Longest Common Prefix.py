#14. Longest Common Prefix
strs = ["flower","flow","flight"]
result = strs[0]
for i in strs:
    temp = []
    for j in range(min(len(i),len(result))):
        if i[j] == result[j]:
            temp.append(i[j])
        else:
            break
    result = "".join(temp)
print(result)
