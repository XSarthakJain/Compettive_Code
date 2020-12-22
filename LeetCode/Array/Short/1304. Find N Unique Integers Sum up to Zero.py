#1304. Find N Unique Integers Sum up to Zero
n=5
result=[]
for i in range(n-1,((n//2))if n&1 else ((n//2)-1),-1):
    result.append(i)
    result.append(i*-1)
if n&1:
    result.append(0)
result.sort()
print(result)
