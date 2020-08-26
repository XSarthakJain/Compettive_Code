#Find Armstrong Number

n=input()

lnth=len(n)
sum=0
temp=1
for i in n:
    print(i)
    sum=sum+(int(i)**lnth)

print(sum)
if sum==int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
        
    
    
