#496. Next Greater Element I
nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]

result = []
for i in nums1:
    flag = True
    for index,item in enumerate(nums2):
        if item == i:
            if nums2[index+1] > item:
                result.append(nums2[index+1])
                flag = False
                break
            else:
                continue
    if flag:
        result.append(-1)
print(result)
