#1629. Slowest Key
releaseTimes = [10,19,20,21,22,32]
keysPressed = "abodzo"
result = dict()
pointer = 0
for index,item in enumerate(keysPressed):
    if item in result:
        result[item] = max(releaseTimes[index] - pointer,result[item])
    else:
        result[item] = releaseTimes[index] - pointer
    pointer = releaseTimes[index]
high = []
for i in keysPressed:
    if result[i] == max(result.values()):
        high.append(i)
print("Result = ",max(high))

    
