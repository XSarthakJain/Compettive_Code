#parenBit
'''
Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".


parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
'''

def parentBit(s):
    if s[0]==")":
        return ")"
    elif len(s)==1:
        return (")" if s[0]==")" else "")
    else:
        return ((s[0:s.index(")")]+parentBit(s[(s.index(")")):]))if s[0]=="(" else (parentBit(s[1:])))



s=input()
print(parentBit(s))
                
