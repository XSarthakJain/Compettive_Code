#1189. Maximum Number of Balloons
text = "Leetcode"
d = dict()
total = 0
formed = dict()
for i in "balloon":
    if i not in formed:
        formed[i] = 1
        d[i] = 0
    else:
        formed[i] += 1
    
for i in text:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
result = d["b"]//formed["b"]
for i in formed:
    if result > d[i]//formed[i]:
        result = d[i]//formed[i]
print(result)
        
