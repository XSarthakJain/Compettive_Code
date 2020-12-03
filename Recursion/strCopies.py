#strCopies

'''
Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.


strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true

'''



def strCopies(s,m,c):
    if len(s)==len(m):
        return ((True)if ((s==m and (c==1)) or (c==0 and s!=m)) else (False))
    else:
        return ((strCopies(s[1:],m,c-1))if s[:len(m)]==m else (strCopies(s[1:],m,c)))
    
    



s=input()
m=input()
print(strCopies(s,m,2))
