#1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
n=int(input())


result = []
def fibo(n1):
    a=1
    b=1
    c=1
    while(True):
        a=b
        b=c
        c=a+b
        if a>n1:
            return (b-a)
            break
c=0
while(True):
    n = n-fibo(n)
    c+=1
    if n == 0:
        break
print(c)
    
