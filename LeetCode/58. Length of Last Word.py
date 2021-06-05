#58. Length of Last Word
s = "a "
temp = s[-1::-1].strip().split(" ")
print(0 if len(temp)<0 else len(temp[0]))
