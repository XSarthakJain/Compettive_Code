#countHi2

'''
Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.


countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
'''

def countHi2(s):
    if len(s)<=3:
        return ((1)if (len(s)>=2 and (s[-1]=="i" and s[-2]=="h" and s[0]!="x")) else (0))
    elif s[0:3]=="xhi":
        return (0+countHi2(s[2]))
    else:
        return ((1+countHi2(s[2:])) if (s[0:2]=="hi") else (0+countHi2(s[1:])))





s=input()
print(countHi2(s))
