class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = dict()
        output = []
        for i in nums1:
            if i not in d:
                s = [1,0]
                d[i] = s
            else:
                d[i][0] = d[i][0] + 1
        for j in nums2:
            if j in d:
                d[j][1]+=1
        for i in d:
            if len(d[i]) == 2 and d[i][1]!=0:
                for j in range(min(d[i][0],d[i][1])):
                    output.append(i)
        return output
                
                
        
