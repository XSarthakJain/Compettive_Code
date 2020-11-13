
n=int(input())
cont=0
for i in range(n):
    temp=input()
    if temp.isdigit() and len(temp)==10:
        cont+=1
print(cont)
