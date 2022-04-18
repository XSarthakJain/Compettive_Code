#2114. Maximum Number of Words Found in Sentences
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result = 0
        for i in sentences:
            if len(i.split())>result:
                result = len(i.split())
        return result
