#128. Longest Consecutive Sequence
nums = [100,4,200,1,3,2]
result = 0

#Optimal Solution
data = set(nums)
for i in range(len(nums)):
    if nums[i]-1 not in data:
        temp_result = 0
        temp=nums[i]
        while(temp in data):
            temp+=1
            temp_result+=1
        result = max(result,temp_result)
print(result)

#Brute Force Approach
'''
nums.sort()
if len(nums)==0:
    print(0)
pivot = nums[0]
temp_result = 1
for i in range(1,len(nums)):
    if nums[i] == pivot+1:
        temp_result+=1
    elif nums[i] == pivot:
        pass
    else:
        result = max(result,temp_result)
        temp_result = 1
    pivot = nums[i]
result = max(result,temp_result)
print(result)
'''
