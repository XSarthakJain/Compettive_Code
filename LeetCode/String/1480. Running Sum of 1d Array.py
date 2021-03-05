#1480. Running Sum of 1d Array
nums = [1,2,3,4]
output = []
high=0
for i in nums:
    output.append(high+i)
    high+=i
print(output)
