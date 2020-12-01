#powerN
'''
Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27
'''

def powerN(n,p):
    if p==0:
        return 1
    else:
        return n*powerN(n,p-1)
        


n=int(input())
p=int(input())
print(powerN(n,p))
