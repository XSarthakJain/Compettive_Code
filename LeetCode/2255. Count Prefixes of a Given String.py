#2255. Count Prefixes of a Given String
words = ["a","b","c","ab","bc","abc"]
s = "abc"
result = 0
for i in words:
    if len(i)<=len(s):
        if s[0:len(i)] == i:
            result+=1
print("Result =",result)
