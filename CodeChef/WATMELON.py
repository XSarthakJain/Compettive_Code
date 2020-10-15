#Problem Code:WATMELON
# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    sum=0
    for i in range(N):
        sum+=A[i]
    if sum>=0:
        print("YES")
    else:
        print("NO")
