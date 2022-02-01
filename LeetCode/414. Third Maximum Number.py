#414. Third Maximum Number
nums = [3,2,1]
first = -float('inf')
second = first
third  = first
temp = first
for i in range(len(nums)):
    if nums[i] > first:
        third = second
        second = first
        first = nums[i]
    elif nums[i] > second and nums[i]!=first:
        third = second
        second = nums[i]
    elif nums[i] > third and nums[i]!=second and nums[i]!=first:
        third = nums[i]
print(third if third!=temp else first)
