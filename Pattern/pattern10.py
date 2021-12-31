nRow = 4
nCol = 4

count = 65
for row in range(1,nRow+1):
    for col in range(1,nCol+1):
        print(chr(count),end="")
        count+=1
    print("")
