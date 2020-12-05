#nestParen
'''
Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.


nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
'''


def nestParent(s):
    if len(s)==1:
        return True
    else:
        return ((nestParent(s[1:]))if ((s[0]=="(" or s[0]==")") and (s[1]==")" or s[1]=="(")) else (False))



s=input()
print(nestParent(s))
