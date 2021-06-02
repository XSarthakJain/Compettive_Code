#28. Implement strStr()
haystack = ""; needle = ""

result = -1
if len(needle) < 1:
    print(0)
for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)] == needle:
        result = i
        break

print(result)


    
