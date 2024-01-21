#13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtype = 0
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        temp = roman[s[0]]
        for index,item in enumerate(s):
            if index>0:
                if temp<roman[item]:
                    temp=roman[item]-temp
                else:
                    rtype+=temp
                    temp = roman[item]
        return rtype+temp
