#1442. Count Triplets That Can Form Two Arrays of Equal XOR
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c=0
        for i in range(len(arr)-1):
            a=0
            for j in range(i+1,len(arr)):
                a=a^arr[j-1]
                b=0
                for k in range(j,len(arr)):
                    b=b^arr[k]
                    if a == b:
                        c+=1
        return c
        
