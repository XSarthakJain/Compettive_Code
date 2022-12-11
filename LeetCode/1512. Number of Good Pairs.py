#1512. Number of Good Pairs
nums = [1,2,3,1,1]
result = 0
contain = dict()
for i in nums:
    if i not in contain:
        contain[i] = 1
    else:
        contain[i]+=1
for i in contain:
    result+= ((contain[i]-1)*contain[i])//2
print(result)
