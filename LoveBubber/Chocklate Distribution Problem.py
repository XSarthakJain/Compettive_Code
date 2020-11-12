#Chocklate Distribution Problem
#code
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    M=int(input())
    A.sort()
    result=A[M-1]-A[0]
    current=0
    for i in range(N):
        if i>=M-1:
            
            result=min(result,A[i]-A[current])
            current+=1
    print(result)
 
