#Find the Union and Interection of two Sorted Array
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))


'''
First Method
s=set()
for i in A1:
    s.add(i)
for i in A2:
    s.add(i)

intersection=dict()
for i in s:
    intersection[i]=i
intersectionList=[]
for i in range(len(A1)):
    if i in intersection:
        intersectionList.append(A1[i])
    

print("Union",s)
print("Intersection",intersectionList)
'''

#Second Method
s1=set()
for i in A1:
    s1.add(i)
s2=set()
for i in A2:
    s2.add(i)
print("union",*(s1.union(s2)))
print("intersection",*(s1.intersection(s2)))
