nums = [1,2,3,4]

min_num = nums[0]
max_num = nums[0]
output = 0
temp_output = 0
for i in range(len(nums)):
    if (max_num - nums[i]) != 1 and (max_num != nums[i]):
        print(min_num,max_num,nums[i])
        if output < temp_output:
            output = temp_output
        temp_output = 0
        min_num = nums[i]
        max_num = nums[i]
    elif (min_num - nums[i]) != 1 and (min_num != nums[i]):
        if output < temp_output:
            output = temp_output
        temp_output = 0
        min_num = nums[i]
        max_num = nums[i]
        
    temp_output+=1


output = max(temp_output,output)
print(output)        
