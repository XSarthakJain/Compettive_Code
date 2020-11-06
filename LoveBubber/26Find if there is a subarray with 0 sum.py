#Find if there is a subarray with 0 sum
#https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
N=list(map(int,input().split()))
s=set()
sum=0
flag=True
for i in N:
    sum+=i
    
    if (sum in s) or (sum==0):
        print("Yes")
        flag=False
        break
    s.add(sum)
    
if flag:
    print("No")
    
