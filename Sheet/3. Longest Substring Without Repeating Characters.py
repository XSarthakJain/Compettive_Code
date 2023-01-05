#3. Longest Substring Without Repeating Characters
s = "abcabcbb"
#Optimal Solution
pt = 0
result = 0
data =dict()
for i in range(len(s)):
    if s[i] in data:
        if data[s[i]]>=pt:
            pt = data[s[i]]+1
    data[s[i]] = i
    result = max(result,i-pt+1)
print(result)

#Another Solution
'''
result = 0
data = []
for i in range(len(s)):
   if s[i] in data:
       result = max(result,len(data))
       data = data[data.index(s[i])+1:]
   data.append(s[i])
print(max(result,len(data)))
'''
#Brute Force Approach
'''
result = 0
for i in range(len(s)):
    temp = []
    temp_result = 1
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp.append(s[j])
            result = max(result,temp_result)
        else:
            break
        temp_result+=1
print(result)
'''
