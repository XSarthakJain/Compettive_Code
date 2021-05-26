nums = list(map(int,input().split()))
target = int(input())

for i in range(len(nums)):
    if (target-nums[i]) in nums:
        if (target-nums[i])==nums[i]:
            if nums.count((target-nums[i])) > 1:
                result = []
                result.append(i)
                result.append((nums[i+1:len(nums)].index((target-nums[i])))+i+1)
                print(result,i+1,nums[i+1:len(nums)])
        else:
            result=[]
            result.append(i)
            result.append(nums.index((target-nums[i])))
            print(result)
