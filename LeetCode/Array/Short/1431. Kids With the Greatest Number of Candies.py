#1431. Kids With the Greatest Number of Candies
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output=[]
        highest=max(candies)
        for i in candies:
            (output.append(True))if (i+extraCandies>=highest) else (output.append(False))
            
        return output
