#Find the Majority Element that occurs more than N/2 times
nums = [3,2,3]
pointer = 0
result = nums[0]
for i in nums:
    if pointer == 0:
        result = i
        pointer+=1
    else:
        if i == result:
            pointer+=1
        else:
            pointer-=1
print("Result = ",result)
