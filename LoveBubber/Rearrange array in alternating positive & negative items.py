#Rearrange array in alternating positive & negative items with O(1) extra space | Set 1
n=list(map(int,input().split()))
posi=[]
negi=[]
for i in range(len(n)):
    if n[i]>=0:
        posi.append(n[i])
    else:
        negi.append(n[i])
l=len(n)

n=[]      
for i in range(l):
    #print(negi[i],posi[i],len(negi),len(posi))
    if i<len(negi):
        n.append(negi[i])
    if i<len(posi):
        n.append(posi[i])
print(n)
        
        
    
