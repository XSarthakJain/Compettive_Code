#Merge two sorted Array Without using Extra Space
A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A1_indi=0
A2_indi=0
for i in range(len(A1)):
    if A2[A2_indi]<A1[A1_indi]:
        A2[A2_indi],A1[A1_indi]=A1[A1_indi],A2[A2_indi]
        A2.sort()
    A1_indi+=1
A2.sort()
print(*A1,*A2)

#With Taking Space we take n+m size Array and put all the value into it and
#after that sort 3rd Array and than Assign back to its orignal array
    
    
        
