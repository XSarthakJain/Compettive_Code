A = input()
d = dict()
for i in A:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
for j in A:
    if d[j] == 1:
        print("non repeative Character",j)
        break
