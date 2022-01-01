nRow = 4
nCol = 4

for row in range(nRow):
    print(" "*(nRow-row-1),end="")
    for col in range(1,row+2):
        print(col,end="")
    if row!=0:
        for col1 in range(row,0,-1):
            print(col1,end="")
    print("")
