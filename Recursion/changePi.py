# changePi
'''
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".


changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"
'''

def changePi(s,l,u):
    if l==u:
        return s[l]
    elif l==u-1:
        return (str(3.14) if s[l]=="p" and s[l+1]=="i" else s[l]+s[l+1])
    elif s[l]=="p" and s[l+1]=="i":
        return str(3.14)+changePi(s,l+2,u)
    else:
        return s[l]+changePi(s,l+1,u)

s=input()
print(changePi(s,0,len(s)-1))
