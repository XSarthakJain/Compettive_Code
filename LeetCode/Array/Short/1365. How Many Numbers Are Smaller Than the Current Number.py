#1365. How Many Numbers Are Smaller Than the Current Number
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output=[]
        for i in nums:
            incre=0
            for j in nums:
                if i>j:
                    incre+=1
            output.append(incre)
        return output
