#1417. Reformat The String
s = "a0b1c2"
output = []
ch = []
dig = []
for i in s:
    if ord(i)>=48 and ord(i)<=57:
        dig.append(i)
    else:
        ch.append(i)
if abs(len(dig)-len(ch)) <= 2 and len(dig) > 0 and len(ch) > 0:
        
    for i in range(max(len(ch),len(dig))):
        if len(dig) > len(ch):
            output.append(dig[i])
            if i < len(ch):
                output.append(ch[i])
        else:
            output.append(ch[i])
            if i < len(dig):
                output.append(dig[i])
print(output)
for i in range(len(output)-1):
    if abs(ord(output[i]) - ord(output[i+1])) < 26:
        print(ord(output[i])-ord(output[i+1]))
        del output
        output = []
        output.append("")
        break
print("".join(output))
