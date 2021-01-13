#1160. Find Words That Can Be Formed by Characters
words = words = ["cat","bt","hat","tree"]; chars = "atach"
c=0
for i in words:
    d = dict()
    for j in chars:
        if j in d:
            d[j]+=1
        else:
            d[j] = 0
    flag = True
    for k in i:
        if k not in d:
            flag = False
            break
        else:
            if d[k] == 0:
                del d[k]
            else:
                d[k] = d[k]-1
    if flag:
        c = c + len(i)
print(c)
