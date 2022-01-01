nRow = 4
nCol =4

for row in range(nRow):
    # Print Space
    for space in range(nRow-row-1):
        print(" ",end="")
    #Print Character
    print("*"*(row+1),end="\n")
    
