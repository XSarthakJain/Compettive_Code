# noX
'''
Given a string, compute recursively a new string where all the 'x' chars have been removed.


noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
'''

def noX(s,l,u):
    if l==u:
        return ("" if s[l]=="x" else s[l])
    elif s[l]=="x":
        return ""+noX(s,l+1,u)
    else:
        return s[l]+noX(s,l+1,u)

s=input()
print(noX(s,0,len(s)-1))
