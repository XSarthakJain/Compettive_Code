nRow = 4
nCol = 4

count = 1
for row in range(nRow):
    for col in range(0,row+1):
        print(count, sep="",end="")
        count+=1
    print("")
