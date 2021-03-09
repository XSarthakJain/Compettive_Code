#1309. Decrypt String from Alphabet to Integer Mapping
s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
output = []
end = -1
for i in range(len(s)):
    if i+2 < len(s):
        if i > end:
            if s[i+2] == "#":
                output.append(chr(96+int(s[i:i+2])))
                end = i+2
            else:
                output.append(chr(96+int(s[i])))
    elif i > end:
        output.append(chr(96+int(s[i])))
print("".join(output))

