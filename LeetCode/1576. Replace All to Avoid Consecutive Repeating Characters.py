#1576. Replace All ?'s to Avoid Consecutive Repeating Characters

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        fixedString = "abc"
        def uniqueCh(prev,next):
            for i in fixedString:
                if (i!=prev and i!=next):
                    return i

        for index,i in enumerate(s):
            if i=="?":
                if index==0:
                    temp = s[index+1] if len(s)>1 else "b" 
                    result.append(uniqueCh("a",temp))
                elif index == (len(s)-1):
                    temp = result[index-1]
                    result.append(uniqueCh(temp,"a"))
                else:
                    result.append(uniqueCh(result[index-1],s[index+1]))

            else:
                result.append(i)
        return "".join([item for item in result])
