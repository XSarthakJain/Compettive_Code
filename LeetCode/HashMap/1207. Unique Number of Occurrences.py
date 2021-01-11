#1207. Unique Number of Occurrences
arr = [1,2]
d = dict()
for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
s=set()

flag = True
for i in d:
    if d[i] in s:
        flag = False
        break
if flag:
    print(True)
else:
    print(False)
