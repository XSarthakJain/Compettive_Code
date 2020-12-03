#strCount

'''
Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.


strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0

'''

def strCount(s,m):
    if len(s)<len(m):
        return 0
    else:
        return ((1+int(strCount(s[len(m):],m)))if (s[0:len(m)]==m) else (0+int(strCount(s[1:],m))))




s=input()
m=input()
print(strCount(s,m))
