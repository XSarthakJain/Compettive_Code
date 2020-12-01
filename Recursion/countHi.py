#countHi
'''
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.


countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
'''

def countHi(s,l,u):
    if l==u-1:
        return (1 if s[l]=="h" and s[u]=="i" else 0)
    elif s[l]=="h" and s[l+1]=="i":
        return 1+countHi(s,l+1,u)
    else:
        return countHi(s,l+1,u)

s=input()
print(countHi(s,0,len(s)-1))
