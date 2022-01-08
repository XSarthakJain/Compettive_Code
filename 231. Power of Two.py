n = int(input())
result = True
        
if n<1:
    return False
else:
    while(n!=1 and n>1):
        if n&1:
            result = False
            break
        else:
             n = n>>1
print(result)
