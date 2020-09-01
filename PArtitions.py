A=5
B=[1,2,3,0,3]
cou=0
for i in range(1,A):
    print("i value = ",i)
    for j in range(i+1,A):
        
       
        if int(sum(B[:i]))==int(sum(B[i:j])) and int(sum(B[i:j]))==int(sum(B[j:])):
            cou+=1
print(cou)
#print("sum(B[1:1])",sum(B[b
