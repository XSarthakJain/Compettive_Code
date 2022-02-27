#66. Plus One
digits = [1,2,3]

add = 1
for ind,item in enumerate(reversed(digits)):
    item+=add
    
    
    if item>9:
        add = item-9
        digits[len(digits)-ind-1] = 0
    else:
        digits[len(digits)-ind-1] = item
        add=0
        break
if add!=0:
    digits.insert(0,add)  
print(digits)
        
