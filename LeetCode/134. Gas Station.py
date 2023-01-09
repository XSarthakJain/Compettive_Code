#134. Gas Station
gas = [2,3,4]
cost = [3,4,3]

result = -1
i = 0
while(i<len(gas)):
    pointer = i
    temp = gas[i]
    count = 0
    flag = True
    while(pointer<len(gas)):
        if temp != 0:
            temp = temp - cost[pointer] + gas[(pointer+1)%(len(gas))]
        elif temp == 0:
            flag = False
            break
        if pointer == i-1:
            break
        
        print("temp = ",temp)
        print(pointer,temp,cost[pointer],gas[(pointer+1)%(len(gas))])
        pointer+=1
        pointer = pointer%(len(gas))
        
    if flag:
        result = i
        break
    i+=1
    print("i =",i)
print("result",result)
