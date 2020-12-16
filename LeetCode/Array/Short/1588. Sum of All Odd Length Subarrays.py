#1588. Sum of All Odd Length Subarrays
arr=list(map(int,input().split()))
output=0
for i in range(len(arr)):
            temp=0
            for j in range(i,len(arr),2):
                temp+=sum(arr[i:j+1])
            output+=temp
print(output)
