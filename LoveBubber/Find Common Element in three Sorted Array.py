#Find Common Element in three Sorted Array

#First Approach
A1=set(map(int,input().split()))
A2=set(map(int,input().split()))
A3=set(map(int,input().split()))

print(*A1.intersection(A2.intersection(A3)))

#Second Approach
'''
Input in list
s1=set()
s2=set()
s3=set()
for i in A:
    s1.add(i)
for i in B:
    s2.add(i)
s3=s1.intersection(s2)
s1=set()
for i in C:
    s1.add(i)
return sorted(list(s3.intersection(s1)))
            
            
'''
