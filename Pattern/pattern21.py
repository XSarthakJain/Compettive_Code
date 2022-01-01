nRow = 4
nCol = 4

for row in range(nRow,0,-1):
    #Space print
    for space in range(nRow-row,0,-1):
        print(" ",end="")
    #Print Character
    for col in range(nRow-row+1, nCol+1):
        print(col,end="")
    print("")
