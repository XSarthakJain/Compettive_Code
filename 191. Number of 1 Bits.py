#191. Number of 1 Bits
n = int(input())
count = 0
while(n!=0):
    if(n&1):
        count+=1
    n = n>>1
    print(count,n)
print(count)
