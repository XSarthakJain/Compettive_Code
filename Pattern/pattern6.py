nRow = 4
nCol = 4

count = 1
for row in range(1,nRow+1):
    #Method 1
    '''
    count = row
    for col in range(1,row+1):
        print(count,end="")
        count+=1
    '''
    #Method 2
    for col in range(0,row):
        print(row+col,end="")
    print("")
