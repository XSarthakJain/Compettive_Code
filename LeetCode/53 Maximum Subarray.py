#53 Maximum Subarray
nums = [5,4,-1,7,8]
sum = nums[0]
temp = 0
for i in nums:
    temp+=i
    sum = max(sum,temp)
    if temp<0:
        temp = 0
print(sum)
     
    
