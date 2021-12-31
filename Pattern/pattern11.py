nRow = 4
nCol = 4

for row in range(1,nRow+1):
    for col in range(1,nCol+1):
        print(chr(63+row+col),end="")
    print("")
