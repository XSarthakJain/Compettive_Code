#changeXY
'''
Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.


changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
'''

def changeXY(s,l,u):
    if l==u:
        return ("y" if s[l]=="x" else s[l])
        
    elif s[l]=="x":
        
        return "y"+changeXY(s,l+1,u)
    else:
        
        return s[l]+changeXY(s,l+1,u)

s=input()
print(changeXY(s,0,len(s)-1))
