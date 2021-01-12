#1002. Find Common Characters
A = ["bella","label","roller"]
result = []
temp = list(set(A[0]))
for i in temp:
    c=A[0].count(i)
    for j in A:
        c = min(c,j.count(i))
    if c != 0:
        for k in range(c):
            result.append(i)

print(result)
