x = int(input())
result = 0
if(x<=(-2**31) or x>=((2**(31)-1))):
    print("0")
else:
    digitSign = 1
    if x<0:
        digitSign = -1
        x = abs(x)
    while(True):
        mod = x%10
        result = result*10 + mod
        x = x//10
        if x<=0:
            break
        if(result<=(-2**31) or result>=((2**(31)-1))):
                return 0
    print(result*digitSign)
