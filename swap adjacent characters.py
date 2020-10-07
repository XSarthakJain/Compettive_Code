s=input()
n=len(s)
ans=""
if n&1:
    print("impossoible")
else:
    odd=1
    even=0
    for i in range(n//2):
        ans+=s[odd]
        ans+=s[even]
        odd+=2
        even+=2
    print(ans)
