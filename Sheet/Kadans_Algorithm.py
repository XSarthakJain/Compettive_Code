#53. Maximum Subarray
nums = [-2,1,-3,4,-1,2,1,-5,4]
sum = 0
tot = nums[0]
for i in range(len(nums)):
    sum+= nums[i]
    if sum>tot:
        tot = sum
    if sum < 0:
        sum = 0
print(tot)
