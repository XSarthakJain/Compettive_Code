#Count the number of subarrays with given xor K
nums = [5]
target = 5
result = 0
for i in range(len(nums)):
    temp = 0
    for j in range(i,len(nums)):
        temp =temp ^ nums[j]
        if temp == target:
            result+=1
print(result)
        
    
