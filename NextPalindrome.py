#Give Input Palindrome Number and it find next Palindrome in O(1)


n=input()

if len(n)==1:
    if int(n)==9:
        print(11)
    else:
        print(int(n)+1)

elif len(n)==2:
    if int(n[0])==9:
        print(101)
    else:
        
        print(str(int(n[0])+1)+str(int(n[1])+1))

elif len(n)>=3:
    if len(n)%2!=0:
        if int(n[len(n)//2])<9:
            print( n[:(len(n)//2)]  + str(int(n[(len(n)//2)])+1)  +(n[((len(n)//2)+1):len(n)]))            
        else:
            mid=int((len(n)//2))
            print(str(int(n[0:mid])+1)+"0"+ str((str(int(n[0:mid])+1))[::-1]))
    else:
        print(str(int(n[:(len(n)//2)])+1) + (str(int(n[:(len(n)//2)])+1))[::-1])
        
        
            
        
    
    
