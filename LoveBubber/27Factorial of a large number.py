#Factorial of a large number
n=int(input())
result=1
for i in range(1,n+1):
    result=result*i
print("Factorial of = ",n," = ",result)
