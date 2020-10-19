#Kth smallest element
A=list(map(int,input().split()))
K=int(input())
A=sorted(A)
print(A[K-1])
