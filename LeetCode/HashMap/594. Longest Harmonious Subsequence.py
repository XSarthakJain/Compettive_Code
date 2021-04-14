nums = [1,1,1,1,1,1,1,1,1,1,1]

d = dict()
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
keySorted = sorted(d.keys())
output = 0
for i,v in enumerate(keySorted[:-1]):
    if keySorted[i]-keySorted[i+1] == -1:
        output = max(output,(d[keySorted[i]]+d[keySorted[i+1]]))
print(output)




























'''
for i in range(len(nums)):
    if (max_num - nums[i]) != 1 and (max_num != nums[i]):
        print(min_num,max_num,nums[i]) 
        if max_num == min_num:
            max_num = max(max_num,nums[i])
            min_num = min(min_num,nums[i])
        else:
            if output < temp_output:
                output = temp_output
            temp_output = 0
            min_num = nums[i]
            max_num = nums[i]
    elif (nums[i]-min_num) != 1 and (min_num != nums[i]) and min_num!=max_num:
        print("Second",min_num,max_num)
        if output < temp_output:
            output = temp_output
        temp_output = 0
        min_num = nums[i]
        max_num = nums[i]
        print("Second",min_num,max_num)
        
    temp_output+=1


output = max(temp_output,output)
print(output)        

'''
