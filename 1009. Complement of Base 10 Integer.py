#1009. Complement of Base 10 Integer
n = int(input())
result = []
while(n!=0):
    if(n&1):
        result.append("0")
    else:
        result.append("1")
    n = n>>1
print(int(("".join(result[::-1])),2))
