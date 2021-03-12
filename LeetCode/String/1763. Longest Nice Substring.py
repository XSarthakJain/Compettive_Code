class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def nice_String(string):
            hashset = set()
            if len(string) < 2:
                return ""
            else:
                for i in range(len(string)):
                    if not (string[i].lower() in hashset and string[i].upper() in hashset:
                            string1 = nice_String(string[:i])
                            string2 = nice_String(string[i:])
                            return string2 if len(string1)< len(string2) else string1
            return string
