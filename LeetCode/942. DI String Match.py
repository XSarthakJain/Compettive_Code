942. DI String Match
s="IDID"
low,high = 0,len(s)
result = []
for i in s:
    if i == "I":
        result.append(low)
        low+=1
    else:
        result.append(high)
        high-=1
result.append(high)
print("Result =",result)
