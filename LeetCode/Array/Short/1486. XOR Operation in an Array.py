#1486. XOR Operation in an Array
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        result=0
        for i in range(n):
            temp=start+2*i
            result=result^temp
        return result
