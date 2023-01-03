#Length of the longest subarray with zero Sum
N = 6
nums = [9, -3, 3, -1, 6, -5]
result = 0

#Optimal Approach
data = dict()
total = 0
for i in range(len(nums)):
    total+= nums[i]
    if total == 0:
        result = i+1
    elif total not in data:
        data[total] = i
    else:
        result = max(result,i-data[total])
print(result)
        

    
#Brute Force Approach
'''
for i in range(len(nums)):
    temp = 0
    ind = 1
    for j in range(i,len(nums)):
        temp+=nums[j]
        if temp == 0:
            result = max(result,ind)
        ind+=1
        
print(result)
'''
