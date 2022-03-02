#415. Add Strings
num1 = "1"
num2 = "9"
carry = 0
i = len(num1)-1
j = len(num2)-1
output = []
while(i>=0 or j>=0 or carry>0):
    if i>=0:
        carry += ord(num1[i])-ord("0")
        print("ord(num1[i])-ord(0)",ord(num1[i])-ord("0"))
        i-=1
    if j>=0:
        carry += ord(num2[j])-ord("0")
        print("ord(num2[j])-ord(0)",ord(num2[j])-ord("0"))
        j-=1
    output.append(str(carry%10))
    carry //=10
    print(output,carry)
print("Output = ","".join(output)[::-1])
        
