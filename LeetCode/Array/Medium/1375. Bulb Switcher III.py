#1375. Bulb Switcher III
light = [2,1,4,3,6,5]
result = []
c = 0
last = 0
val=0
for i in range(len(light)):
    result.append(0)
for i in light:
    val+=1
    result[i-1] = 1
    flag = False
    #Left Blue Bulb
    last = max(last,i)
    if last == val:
        c+=1
print(c)
