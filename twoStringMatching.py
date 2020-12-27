s1="This is a test String"
s2="tsit"
s1=s1.lower()
d1=dict()
c2=0
for i in s1:
    d1[i]=s1.count(i)
flag=False
while(True):
    for i in s2:
        if i in d1:
            d1[i]-=1
            if d1[i]==0:
                del d1[i]
        else:
            flag=True
            break
    if flag:
        break
    c2+=1
print(c2)

    
