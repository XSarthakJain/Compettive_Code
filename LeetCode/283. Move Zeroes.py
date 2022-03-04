#283. Move Zeroes
nums = [0,1,0,3,12]
ind = 0
for i in range(len(nums)):
    if nums[ind] == 0:
        del nums[ind] 
        nums.append(0)
    else:
        ind+=1
