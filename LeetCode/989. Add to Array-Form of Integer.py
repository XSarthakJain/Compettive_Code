#989. Add to Array-Form of Integer
num = [2,1,5]
k = str("806")

output = []
p=1
carry = 0
while(p<=max(len(num),len(k))):
    result0 = 0
    result1= 0
    if len(num)>=p:
        result0 = int(num[len(num)-p])
    if len(k)>=p:
        result1= int(k[len(k)-p])
    temp = str(result0 + result1 + int(carry))
    print("temp",temp,result0,result1,carry)
    if len(str(temp))>1:
        temp0 = temp
        carry = temp0[:len(temp0)-1]
        temp = temp[-1]
    else:
        carry = 0
    output.append(temp)
    p+=1

if int(carry)>0:
    output.append(carry)
output.reverse()
print(output)
