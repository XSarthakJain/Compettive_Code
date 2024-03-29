#18. 4Sum
nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()
result = []

#Optimal Solution
for i in range(0,len(nums)-2):
    for j in range(i+1,len(nums)-1):
        left = j+1
        right = len(nums)-1
        desire_ele = target - nums[i]-nums[j]
        while(left<right):
            if nums[left]+nums[right] == desire_ele:
                temp = [nums[i],nums[j],nums[left],nums[right]]
                print([nums[i],nums[j],nums[left],nums[right]])
                temp.sort()
                print(temp)
                if temp not in result:
                    result.append(temp)
                temp_left = nums[left]
                temp_right = nums[right]
                while(left<right and nums[left]==temp_left):
                    left+=1
                while(left<right and nums[right]==temp_right):
                    right-=1
            elif nums[left]+nums[right] > desire_ele:
                right-=1
            else:
                left+=1
                
        

#Brute Force Approach
'''
for i in range(0,len(nums)-3):
    for j in range(i+1,len(nums)-2):
        for k in range(j+1,len(nums)-1):
            left = k+1
            right = len(nums)-1
            desire_ele = target - nums[i]-nums[j]-nums[k]
            while(left<=right):
                mid = left+(right-left)//2
                if nums[mid] == desire_ele:
                    temp = [nums[i],nums[j],nums[k],nums[mid]]
                    temp.sort()
                    print(temp)
                    if temp not in result:
                        result.append(temp)
                    break
                elif nums[mid]>desire_ele:
                    right = mid-1
                else:
                    left = mid+1

'''              
print("Second Element = ",result)
    


