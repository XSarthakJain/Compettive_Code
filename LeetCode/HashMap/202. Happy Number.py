'''
202. Happy Number
Easy

3059

501

Add to List

Share
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = []
        while(True):
            add = 0
            for i in str(n):
                add+=int(i)*int(i)
            if add == 1:
                return True
            else:
                if add in temp:
                    return False
                else:
                    n = add
                    temp.append(add)
            
