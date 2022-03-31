#1297. Maximum Number of Occurrences of a Substring
subStr = "abcde"
maxLetters = 2
minSize = 3
maxSize = 3

#Submission 1
def subString(s,ch,total):
    if len(s)<len(ch):
        return total
    elif s[:len(ch)] == ch:
        total+=1
    l = len(s)
    return subString(s[1:l],ch,total)

result = 0
for index,item in enumerate(subStr):
    if len(set(subStr[index:index+minSize])) <=maxLetters and len(subStr[index:])>=minSize:
        result = max(result,subString(subStr[index:],subStr[index:index+minSize],int("0")))
        result = max(result,subString(subStr[index:],subStr[index:index+maxSize],int("0")))
print("Result = ",result)
        

    

#Submission 2
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        d = {}
        for i in range(len(s)):
            if len(set(s[i:i+minSize]))<=maxLetters and len(s[i:])>=minSize:
                if s[i:i+minSize] not in d:
                    d[s[i:i+minSize]] = 1
                else:
                    d[s[i:i+minSize]]+=1
        result =0
        for i in d:
            result = max(result,d[i])
        return result
        
        
