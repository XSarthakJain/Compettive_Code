# endX
'''
Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.


endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"

'''

def endX(s):
    if len(s)==1 or s.count("x")==len(s):#s[0]=="r":#(s[0:len(s)]==s[(len(s)-1):0]):
        return s[0:len(s)]
    else:
        return ((endX(s[1:len(s)]+""+s[0])if s[0]=="x" else (s[0]+""+endX(s[1:len(s)]))))



s=input()
print(endX(s))

        
