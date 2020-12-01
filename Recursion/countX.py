#countX
'''
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0
'''
def countX(s,l,u):
    if l==u:
        return (1 if s[l]=="x" else 0)
    elif s[l]=="x":
        return 1+countX(s,l+1,u)
    else:
        return countX(s,l+1,u)

s=input()
print(countX(s,0,len(s)-1))
