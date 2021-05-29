#13. Roman to Integer
s = input()
d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
result = 0
pivot = d[s[-1]]
for ind,i in enumerate(reversed(s)):
    if d[i]<pivot:
        result-=d[i]
    else:
        result+=d[i]
    pivot = d[i]
    print(i,ind)
print(result)
