# Chef and Easy Queries 
# cook your dish here
T=int(input())
for _ in range(T):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    h=A[0]
    i=0
    flag=True
    for i in range(len(A)):
        if h<=k:
            print(i+1)
            break
        elif i!=0:
            h=h+A[i]-k
        else:
            h=h-k
        i+=1

    if i<len(A):
        if h%k!=0:
            print(i+1+h//k)
        else:
            print(i+h//k)
