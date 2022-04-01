#1480. Running Sum of 1d Array
nums = [1,2,3,4]
pointer = 0
for index,item in enumerate(nums):
    nums[index]+=pointer
    pointer = nums[index]
print("Result =",nums)
