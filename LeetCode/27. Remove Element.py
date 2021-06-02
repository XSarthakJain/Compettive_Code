#27. Remove Element
nums = [3,2,2,3]
val = 3
left = 0
right = 0
while(True):
    if right==len(nums):
        break
    if nums[right]!=val:
        nums[left]=nums[right]
        left+=1
        right+=1
    else:
        right+=1
print(nums,left)
        
        
        
        
