class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rtype=''
        pointer = 0
        for index,item in enumerate(strs[0]):
            if len(strs)>1:
                flg = True
                for j_ind in range(1,len(strs)):
                    if strs[0][pointer:index+1] != strs[j_ind][pointer:index+1]:
                        flg = False
                        break
                if not flg:
                    rtype = max(rtype,strs[0][pointer:index])
                    break
                else:
                    rtype = max(rtype,strs[0][pointer:index+1])
            else:
                rtype = strs[0]

                           
        return rtype

                    



        
