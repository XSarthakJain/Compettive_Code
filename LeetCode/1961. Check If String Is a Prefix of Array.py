#1961. Check If String Is a Prefix of Array
s = "iloveleetcode"
words = ["apples","i","love","leetcode"]
result = True
pointer = 0
for i in words:
    if pointer == len(s):
        break
    elif s[pointer:len(i)+pointer] == i:
        pointer+=len(i)
    else:
        result = False
        break
print(False if len(s) != pointer else result)
    
