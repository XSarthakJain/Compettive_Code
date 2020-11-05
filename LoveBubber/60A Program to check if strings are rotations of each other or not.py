#A Program to check if strings are rotations of each other or not
S=input()
S1=input()
#Operation
S=S+S
if S1 in S:
    print(1)
else:
    print(0)
