#905. Sort Array By Parity
A=[3,1,2,4]
even=[]
odd=[]
result=[]
for i in A:
    if i&1:
        odd.append(i)
    else:
        even.append(i)
for i in even:
    result.append(i)
for j in odd:
    result.append(j)
print(result)
