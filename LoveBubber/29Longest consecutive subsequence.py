#Longest consecutive subsequence
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    A=list(set(A))
    A.sort()
    
    counter=1
    maximum=0
    print(A)
    for i in range(len(A)-1):
        if A[i]==(A[i+1]-1):
            counter+=1
        else:
            maximum=max(counter,maximum)
            counter=1
    print(max(counter,maximum))
