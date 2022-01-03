#Find the Two Non Duplicate Numbers
A = [5,4,1,4,3,5,1,2]
result = 0
for item in A:
    result = result ^ item

even = []
odd = []
for item in A:
    if item&1:
        odd.append(item)
    else:
        even.append(item)
temp = result
for item in odd:
    result = result^item
print("Items are =",(temp^result),result)
