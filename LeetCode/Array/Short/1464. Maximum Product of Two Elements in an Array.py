#1464. Maximum Product of Two Elements in an Array
nums = [3,7]
result=1
nums.sort()
nums=nums[::-1]
result=(nums[0]-1)*(nums[1]-1)


print(result)
