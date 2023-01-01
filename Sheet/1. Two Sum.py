#1. Two Sum
nums = [3,2,4]
target = 6
#Dictionary Solution
data = dict()
for i in range(len(nums)):
    if target-nums[i] in data:
        print([i,nums[target-nums[i]]])
        break
    data[nums[i]]=i
    
        
    
#Two Pointer Approach O(nlogn) Time Complexity
'''
left = 0
right = len(nums)-1
dummyList = nums[0:]#O(n) Space
nums.sort() #nlog(n)
for i in range(len(nums)):#O(n)
    if nums[left]+nums[right] == target:
        break
    elif nums[left]+nums[right] > target:
        right-=1
    else:
        left+=1
result = []
for i in range(len(dummyList)):#O(n)
    if dummyList[i] == nums[left] or dummyList[i] == nums[right]:
        result.append(i)
result.sort()
print(result,nums1)
'''
'''
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i,j])
            break
'''
