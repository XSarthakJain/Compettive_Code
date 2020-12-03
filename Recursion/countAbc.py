#countAbc
'''
Count recursively the total number of "abc" and "aba" substrings that appear in the given string.


countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2

'''

def countAbc(s):
    if len(s)<=3:
        return (1 if len(s)==3 and (s=="abc" or s=="aba") else 0)
    else:
        return ((1+countAbc(s[1:len(s)]) )if (s[0:3]=="abc" or s[0:3]=="aba") else (0+countAbc(s[1:len(s)])))


s=input()
print(countAbc(s))
