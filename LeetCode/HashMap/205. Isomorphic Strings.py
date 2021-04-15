class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        temp = set()
        for i in range(min(len(s),len(t))):
            if s[i] not in d:
                if t[i] in temp:
                    return False
                d[s[i]] = t[i]
                temp.add(t[i])
            if d[s[i]] != t[i]:
                return False
        return True
