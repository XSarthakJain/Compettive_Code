#count11
'''
Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.


count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
'''

def count11(s):
    if len(s)<=3:
        return ((1) if s[0:2]=="11" or s[1:3]=="11" else (0))
    else:
        return ((1+(count11(s[2:len(s)])))if s[0:2]=="11" else (0+count11(s[1:len(s)])))



s=input()
print(count11(s))
