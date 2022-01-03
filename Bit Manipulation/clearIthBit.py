n=13
pivotElement = int(input())
mask = n&(~(1<<(pivotElement-1)))
print(mask)
