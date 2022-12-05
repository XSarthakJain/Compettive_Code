#88. Merge Sorted Array
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
if m == 0 and n>0:
    for i in range(len(nums2)):
        nums1[i] = nums2[i]
i = m + n -1
l = m-1
r = n-1
while r>=0:
    if l<0 or nums2[r] > nums1[l]:
        nums1[i] = nums2[r]
        i-=1
        r-=1
    else:
        nums1[i] = nums1[l]
        i-=1
        l-=1
    print(l,r)

print(nums1)
'''
i = 0
j = 0
result = []
nums1 = nums1[:m]
nums1.sort()
nums2.sort()
while i<m and j<len(nums2):
    if nums1[i] > nums2[j]:
        result.append(nums2[j])
        j+=1
    elif nums1[i] < nums2[j]:
        result.append(nums1[i])
        i+=1
    elif nums1[i] == nums2[j]:
        result.append(nums1[i])
        result.append(nums2[j])
        i+=1
        j+=1
    #print(result)
if i<m:
    result.extend(nums1[i:m])
if j<len(nums2):
    result.extend(nums2[j:])
nums1 = result
print(result)
'''    
        
