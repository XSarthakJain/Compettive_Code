#Given a string, print all possible palindromic partitions
'''
Given a string, find all possible palindromic partitions of given string.
'''

result=set()
def palindrome(s,l):
    if l==len(s):
        return
    else:
        for i in range(l,len(s)):
            if s[l:i]==s[i-1:l-1:-1] and len(s[l:i])>1:
                temp1=" "
                temp=temp1.join(s[0:l])+" "+s[l:i]+" "+temp1.join(s[i:])
                result.add(temp)
        return palindrome(s,l+1)
n=input()
palindrome(n,0)
result.add(" ".join(n))
print(*result,sep="\n")
