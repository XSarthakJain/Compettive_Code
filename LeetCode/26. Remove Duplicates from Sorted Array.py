#26. Remove Duplicates from Sorted Array
nums = [1,1,2]

left = 0
right = 0

while(True):
    if right==len(nums):
        break
    if nums[left] != nums[right]:
        left+=1
        nums[left] = nums[right]
    else:
        right+=1
print(nums,left+1)
        
