#821. Shortest Distance to a Character
s = "aaab"
c = "b"
result = []
d = dict()
d[c] = []
for index,i in enumerate(s):
    if i == c:
        d[i].append(index)
        

for index,i in enumerate(s):
    localResult = 100000
    for ele in d[c]:
        localResult = min(localResult,abs(index-ele))
    result.append(localResult)
print("Result =",result)
        
