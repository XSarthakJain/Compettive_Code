A=[]
while(True):
    temp=input()
    if temp=="Q":
        break
    else:
        A.append(temp)
c=0
result=[]
for i in range(len(A)):
    for j in range(i+1,len(A)):
        c+=1
        temp=str(A[i])+"-VS-"+str(A[j])
        result.append(temp)
print("TOTAl MATCHES:",c)
for i in result:
    print(i)
        
        
    
