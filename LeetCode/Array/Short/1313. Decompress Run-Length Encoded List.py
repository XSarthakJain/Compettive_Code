#1313. Decompress Run-Length Encoded List
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(0,len(nums),2):
            if nums[i]>0:
                for j in range(nums[i]):
                    output.append(nums[i+1])
        return output
