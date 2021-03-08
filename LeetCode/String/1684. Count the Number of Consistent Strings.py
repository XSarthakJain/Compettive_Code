#1684. Count the Number of Consistent Strings
allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
total = 0
for i in words:
    flag = True
    for j in i:
        if j not in allowed:
            flag = False
            break
    if flag:
        total+=1
print(total)
