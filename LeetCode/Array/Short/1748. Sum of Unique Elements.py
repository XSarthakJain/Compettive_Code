#1748. Sum of Unique Elements
nums = [1,1,1,1,1]
d = dict()
result = 0
for i in nums:
    if i in d:
        d[i] = d[i]+1
        if d[i] == 2:
            result -= i
    else:
        d[i] = 1
        result+=i
print(result)
