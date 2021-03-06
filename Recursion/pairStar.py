#pairStar
'''
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".


pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"

'''

def pairStar(s):
    if len(s)==1:
        return s[-1]
    else:
        return ((s[0]+"*"+pairStar(s[1:len(s)]) if s[0]==s[1] else (s[0]+pairStar(s[1:len(s)]))))


s=input()
print(pairStar(s))
