#1780. Check if Number is a Sum of Powers of Three
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(14,-1,-1):
            power = pow(3,i)
            if n-power >= 0:
                n = n-power
            if n== 0:
                return True
        return False

obj = Solution()
print(obj.checkPowersOfThree(int(input())))
