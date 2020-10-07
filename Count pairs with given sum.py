#The input is n binary number in n different rows, find the unrepeated binary row.
binary=[]
n=int(input())
for i in range(n):
    binary.append(input())
temp=dict()

'''
1 0 1
0 1 1
1 1 0
'''

for i in binary:
    if i in temp:
        temp[i]=temp[i]+1
    else:
        temp[i]=1

for i in temp:
    if temp[i]==1:
        print(i)
        

        
