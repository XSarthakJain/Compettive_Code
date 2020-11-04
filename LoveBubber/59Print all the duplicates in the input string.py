#Print all the duplicates in the input string
S=input()
h=dict()

#Operation
for i in S:
    if i in h:
        h[i]+=1
    else:
        h[i]=1
#Print
for i in h:
    if h[i]!=1:
        print(i,"-> ",h[i])
