'''
Method 1
# cook your dish here
T=int(input())
for _ in range(T):
    Pc,Pr=map(int,input().split())
    if Pr<=9:
        print("1"+" "+"1")
    elif Pc<=9:
        print("0"+" "+"1")
    else:
        if Pc%9!=0:
            count_c=(Pc//9)+1
        else:
            count_c=Pc//9

        if Pr%9!=0:
            count_r=(Pr//9)+1
        else:
            count_r=Pr//9


        
        if count_c==count_r:
            print("1"+" "+str(min(count_c,count_r)))
        elif count_r<count_c:
            print("1"+" "+str(min(count_c,count_r)))
        else:
            print("0"+" "+str(min(count_c,count_r)))
            
'''
#Method 2
from math import ceil
for _ in range(int(input())):
    pc,pr=map(int,input().split())
    if ceil(pc/9)<ceil(pr/9):
        print(0,ceil(pc/9))
    else:
        print(1,ceil(pr/9))
        
