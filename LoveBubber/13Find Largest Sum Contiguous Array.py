#Find Largest Sum Contiguous Array
A=list(map(int,input().split()))

'''
#First Approach
maximum=A[0]
for i in range(len(A)):
    sum=0
    for j in range(i,len(A)):
        sum+=A[j]
        if maximum<sum:
            maximum=sum
print("Largest Sum ",maximum)
'''


#Kadane Algorithm
maximum=A[0]
sum=0
for i in range(len(A)):
    sum+=A[i]
    if sum<0:
        sum=0
    if sum>maximum:
        maximum=sum
if maximum==0:
    maximum=max(A)
print("Largest Sum ",maximum)
        
        
