#771. Jewels and Stones
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        result = 0
        for i in stones:
            if i in jewels:
                result+=1
        return result
        
