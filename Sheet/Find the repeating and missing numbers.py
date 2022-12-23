#Find the repeating and missing numbers
nums = [3,1,2,5,3]
for i in range(len(nums)):
    if nums[abs(nums[i])-1]<0:
        print("Duplicate Element = ",abs(nums[i]))
        break
    else:
        nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
for i in range(len(nums)):
    if nums[i] > 0:
        print("Missing Element = ",i+1)
        break
        

        
'''
total = len(nums)*(len(nums)+1)//2
temp = 0
for i in nums:
    temp = temp ^ i
print(temp)  
temp = temp & -temp
print(temp)
temp = total- temp #total-temp
for i in nums:
    temp2 = temp - i
    if temp2<=len(nums):
        print("Result = ",i,temp2)
        break
        
    
'''
