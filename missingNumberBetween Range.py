n=list(map(int,input().split()))
start,end=map(int,input().split())
current=start
d=dict()
for i in n:
    d[i]=True

for i in range(start,end+1):
    if i not in d:
        print(i,end=" ")
