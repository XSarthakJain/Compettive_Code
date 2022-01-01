nRow = 4
nCol = 4
for row in range(nRow):
    for col in range(0,row+1):
        print(chr(65+row+col),end="")
    print("")
