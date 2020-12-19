#1295. Find Numbers with Even Number of Digits
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=0
        for i in nums:
            if ((len(str(i))^1)==len(str(i))+1):
                counter+=1
        return counter
                
