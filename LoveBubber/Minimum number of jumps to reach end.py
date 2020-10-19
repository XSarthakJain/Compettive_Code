#Minimum number of jumps to reach end
A=list(map(int,input().split()))
step=0
path=0
for i in range(len(A)):
    s=A[path:path+A[path]+1]
    ind=max(A[path+1:(path+A[path]+1)])
    print("S",s,ind)
    path=path+(s.index(ind))
    print(path)
    step+=1
    if path>=len(A)-1:
        break
print("Minimum Jumps = ",step)
    
    
