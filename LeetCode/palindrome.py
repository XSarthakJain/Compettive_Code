s = input("Enter String :")
result = ""
s = s.upper()
for i in s:
    if ord(i)>=65 and ord(i)<=90:
        result +=i
if len(result)>0:
    print(result[::] == result[::-1])
else:
    print("We need atleast one Character")
