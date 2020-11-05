#Check if a string is a valid shuffle of two strings
S=list(input())
S1=input()
S2=input()

flag=True
ind=0
for i in S1:
    try:
        ind=S.index(i,ind)
        S.remove(i)
    except:
        flag=False
        break
if flag==False:
    print("Not Suffled")
else:
    ind=0
    flag=True
    for i in S2:
        try:
            ind=S.index(i,ind)
            S.remove(i)
        except:
            flag=False
            break
    if flag:
        print("Suffled")
    else:
        print("Not Suffled")
    
    
    
