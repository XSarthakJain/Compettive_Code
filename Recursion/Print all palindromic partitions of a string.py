#Print all palindromic partitions of a string
'''
Given a string s, partition s such that every string of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example :

Input  : s = "bcc"
Output : [["b", "c", "c"], ["b", "cc"]]

Input  : s = "geeks"
Output : [["g", "e", "e", "k", "s"], 
          ["g", "ee", "k", "s"]]
'''

result=[]
def palindrome(s,l):
    if l>len(s):
        return
    else:
        for i in range(l,len(s)+1):
            if s[l:i]==s[i-1:l-1:-1] and len(s[l:i])>1:
                temp1=" "
                tempResult=[]
                if len(temp1.join(s[0:l]))>0:
                    for j in s[0:l]:
                        tempResult.append(j)
                tempResult.append(s[l:i])
                if len(temp1.join(s[i:]))>0:
                    for j in s[i:]:
                        tempResult.append(j)
                if tempResult not in result:
                    result.append(tempResult)
        return palindrome(s,l+1)
n=input()
palindrome(n,0)
temp=[]
for i in n:
    temp.append(i)

result.append(temp)
print(result,sep="\n")
