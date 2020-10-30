#Count pair
n,k=map(int,input().split())
arr=list(map(int,input().split()))
counter=0
for i in range(n):
    sum=arr[i]
    for j in range(i,n):
        if (sum+arr[j])==k:
            print(sum,arr[j],i,j)
            counter+=1
            sum=arr[i]
print(counter)
