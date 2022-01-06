n = int(input())
a=0
b=1
c=a+b
print(a,end="",sep=",")
for i in range(n-1):
    c=a+b
    b=a
    a=c
    print(a,end="",sep=",")
    
