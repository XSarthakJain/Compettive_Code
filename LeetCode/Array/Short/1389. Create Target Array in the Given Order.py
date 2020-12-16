#1389. Create Target Array in the Given Order
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        output=[]
        
        for i in range(len(index)):
            output.insert(index[i],nums[i])
        return output
