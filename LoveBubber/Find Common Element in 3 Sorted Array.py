#https://practice.geeksforgeeks.org/problems/common-elements1132/1
#Find Common Element in 3 Sorted Array

A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A3=list(map(int,input().split()))

s=set()
for i in A1:
    s.add(i)
result=[]
for i in A1:
    if (i in A2) and (i in A3):
        result.append(i)
print(*result)



