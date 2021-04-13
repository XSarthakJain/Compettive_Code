class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        differentcandyType = len(set(candyType))
        return (differentcandyType) if (differentcandyType<=len(candyType)//2) else (len(candyType)//2)
