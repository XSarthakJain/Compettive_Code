nRow = 4
nCol = 4

start = 68
for row in range(nRow):
    for col in range(0,row+1):
        print(chr(start-row+col),end="")
    print("")
