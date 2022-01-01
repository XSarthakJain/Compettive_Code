nRow = 8
nCol = 8

for row in range(nRow,0,-1):
    #First Triangle
    for col in range(1,row+1):
        print(col,end="")
    #Print Start
    if row!=nRow:
        print("*"*((nRow-row)*2),end="")
    #Second Triangle
    for col in range(row,0,-1):
        print(col,end="")
    print("")
