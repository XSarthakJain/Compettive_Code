#1436. Destination City
paths = [["B","C"],["D","B"],["C","A"]]
start = paths[0][1]
while(True):
    temp = start
    for i in paths:
        if i[0] == start:
            start = i[1]
            break
    if temp == start:
        break
print(start)
        
    
