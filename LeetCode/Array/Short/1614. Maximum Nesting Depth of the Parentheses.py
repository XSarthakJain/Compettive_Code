#1614. Maximum Nesting Depth of the Parentheses
s =  "1"
left=[]
c=0
for i in s:
    if i == "(":
        left.append(i)
        c = max(c,len(left))
    elif i == ")":
        left.pop()

print(c)
        
