#Find a specific pair in Matrix
N=int(input())
A=[]
for i in range(N):
    temp=[]
    temp=list(map(int,input().split()))
    A.append(temp)
maximum=0
for i in range(N-1):
    for j in range(N-1):
        for a in range(i+1,N):
            for b in range(j+1,N):
                if maximum<int(A[a][b]-A[i][j]):
                    maximum=int(A[a][b]-A[i][j])
print("Maximum",maximum)
                
