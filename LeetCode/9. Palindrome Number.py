#9. Palindrome Number
x = int(input())
flag = False
if x<0:
    flag = False
else:
    result = 0
    i=x
    while(i>0):
        temp = i%10
        result = result*10+temp
        i=i//10
    if x == result:
        flag = True
print(flag)
