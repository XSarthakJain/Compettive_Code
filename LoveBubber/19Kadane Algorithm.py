#Kadane Algorithm
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    maximum=A[0]
    sum=A[0]
    for i in range(len(A)):
        if i!=0:
            sum+=A[i]
        
            
        if sum<0:
            sum=0
        elif sum>maximum:
            maximum=sum
        
    print(max(maximum,max(A)))
