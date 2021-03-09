#1370. Increasing Decreasing String
s = "aaaabbbbcccc"
s=sorted(s)
#Put into dictionary
d = dict()
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1

output = []
ran = len(s)
for i in range(ran):
    #Step 1,2,3
    
    for j in d:
        if d[j] > 0:
            output.append(j)
            if d[j] == 1:
                d[j] = 0
            else:
                d[j]-=1
    #Step 4,5,6
    for j in reversed(list(d.keys())):
        if d[j] > 0:
            output.append(j)
            if d[j] == 1:
                d[j] = 0
            else:
                d[j]-=1
print("".join(output))
    
