#1221. Split a String in Balanced Strings
s = "RLLLLRRRLR"
R=0
L=0
total=0
for i in s:
    if i == "R":
        R+=1
    else:
        L+=1
    if R == L:
        total+=1
        L=0
        R=0
print(total)
