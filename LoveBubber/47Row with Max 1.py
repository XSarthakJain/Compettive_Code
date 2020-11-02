#Row with Max 1
arr=[[0,1,1,1],[0,0,1,1],[1,0,0,1],[0,0,0,0]]
n=4
count=0
ind=-1
for i in range(n):
    if count<arr[i].count(1):
        count=arr[i].count(1)
        ind=i
print(ind)


#GFG Code https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#
