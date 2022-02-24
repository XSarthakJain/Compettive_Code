#806. Number of Lines To Write String
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
cursor=0
line=1
tempResult = 0
for i in s:
    tempResult=widths[int(ord(i))-97]
    
    if tempResult+cursor>100:
        line+=1
        cursor=0
    cursor+=tempResult
  
print("Result", [line,cursor])
    
