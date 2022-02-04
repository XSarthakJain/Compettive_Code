#984. String Without AAA or BBB
a = 4
b = 1

result = []
while(True):
    if a == 0:
        result.append("b"*b)
        break
    elif b == 0:
        result.append("a"*a)
        break
    elif a>b:
        result.append("aab")
        a=a-2
        b=b-1
    elif b>a:
        result.append("bba")
        b=b-2
        a=a-1
    elif a==b:
        result.append("ab")
        a=a-1
        b=b-1
total = "".join([str(item) for item in result])
    
print("Result = ",total)
