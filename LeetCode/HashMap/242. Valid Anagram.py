class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i]+= 1
        for i in t:
            if i in d and d[i]!=0:
                d[i] = d[i] - 1
            else:
                return False
        for i in d:
            if d[i]!=0:
                return False
        return True
            
