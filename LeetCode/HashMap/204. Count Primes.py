#Seive of Erratosthenes
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = 0
        seive = []
        for i in range(n):
            seive.append(0)
        for i in range(2,n):
            if seive[i] == 0:
                for j in range(i*i,n,i):
                    seive[j] = 1
        for i in range(2,n):
            if seive[i] == 0:
                output+=1
        if n == 2:
            output=0
        
        return output
                    
                    
                    
        

















'''
import math
n = 10
output = 0
for j in range(2,n):
    if j > 1:
        flag = True
        if j%2 == 0 and j!=2:
            flag = False
        else:
            for i in range(3,1+int(math.floor(math.sqrt(j))),2):
                if j%i == 0:
                    flag = False
                    break
        if flag:
            print(j)
            output+=1
print(output)
'''
