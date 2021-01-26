#35. Search Insert Position
nums = [1,3,5,6] ; target = 7
result = len(nums)

for i in range(len(nums)):
    if nums[i] == target:
        result = i
        break
    else:
        if nums[i]>target:
            target = min(target,i)
print(result if result!=len(nums) else len(nums) if target>=nums[-1] else "0" if target<0 else target)
