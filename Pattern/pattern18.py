nRow = 4
nCol =4

for row in range(nRow,0,-1):
    #Python Support
    #print((" "*(nRow-row)),"*"*row)

    #All Language Support
    #Space Print
    for space in range(nRow-row,0,-1):
        print(" ",end="")
    #print Character
    for col in range(row,0,-1):
        print("*",end="")
    print("")
