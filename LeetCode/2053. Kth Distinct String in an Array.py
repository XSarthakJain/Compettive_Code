#2053. Kth Distinct String in an Array
arr = ["d","b","c","b","c","a"]
k = 2
result = dict()
for i in arr:
    result[i] = result[i]+1 if i in result else 1
result = {key:val for key, val in result.items() if val == 1}
try:
    print(list(result)[k-1],result)
except:
    print("")
