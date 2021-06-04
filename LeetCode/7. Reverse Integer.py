#7. Reverse Integer
x = int(input())
result = 0

if x>-2147483648 and x<2147483648:
     for i in str(x):     
         print(x)
         rem = x%10
          result = result*10 + rem
         x = x//10
         print(rem,x)
print(result)

