#448. Find All Numbers Disappeared in an Array
nums = [4,3,2,7,8,2,3,1]
result = []
for i in range(len(nums)):
    if nums[nums[i] - 1] != i:
        print("nums[nums[i] - 1] = ",nums[nums[i] - 1],nums)
        temp = nums[nums[i] - 1]
        nums[nums[i]-1] = nums[i]
        nums[i] = temp
for i in range(len(nums)):
    print("====== ",nums[i],i)
    if nums[i] != i+1:
        result.append(i+1)
print(result)
