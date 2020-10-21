nums=list(map(int,input().split()))
num1=1
for i in nums:
    num1=num1*10+i
left=len(nums)-1
right=len(nums)-1
right_Value=0
while(True):
    if nums[right]>nums[right-1]:
        right_Value=right-1
        break
    else:
        right-=1
left_Value=0
while(True):
    if nums[left]>nums[right_Value]:
        left_Value=left
        break
    else:
        left-=1
nums[right_Value],nums[left_Value]=nums[left_Value],nums[right_Value]
nums[(right_Value+1):len(nums)].sort()
num2=1
for i in nums:
    num2=num2*10+i
if num1>num2:
    nums.sort()
    print(nums)
else:
    print(nums)
        

        
    
