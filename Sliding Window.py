#Sliding Window
A=list(map(int,input().split()))
n=int(input())
sum=0
highest=0
j=0
for i in range(len(A)):
    if i>n-1:
        sum=sum-A[j]+A[i]
        j+=1
        if highest<sum:
            highest=sum
    else:
        sum+=A[i]
        highest=sum
   
if i>=n-1:
    print(highest)
