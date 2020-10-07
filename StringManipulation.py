#aabbacabdd then print it in a4b3c1d2
s=input()
temp=[]
for i in range(0,len(s)):
    if s[i] in temp:
        continue
    else:
        temp.append(s[i])
        sum=0
        for j in range(i,len(s)):
            if s[j]==s[i]:
                sum+=1
        print(s[i]+""+str(sum),end="")
            
#Best Solution
d=dict()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for i in sorted(list(d.keys())):
    print(i,d[i],sep='',end='')
print()



#Output a2b2a1c1a1b1d2
arr=""
last=s[0]
last_count=0
for i in s:
    if i == last:
        last_count+=1
    else:
        arr+=f"{last}{last_count}"
        last=i
        last_count=1
arr+=f"{last}{last_count}"
print(arr)
        
    
    

