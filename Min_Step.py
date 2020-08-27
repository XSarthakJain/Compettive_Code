A=list(map(int,input().split(",")))
B=list(map(int,input().split(",")))
lenth=0
if len(A)>1:
    lnth=min(A[0],B[0])
    for i in range(1,len(A)):
        if min(A[i],B[i])>=0:
            lnth+=min(A[i],B[i])
        else:
            lnth=lnth-min(A[i],B[i])
print(lnth)
