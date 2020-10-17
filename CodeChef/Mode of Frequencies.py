# cook your dish here
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))

    d=dict()
    for i in A:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1

    d1=dict()
            
    for j in d.values():
        if j in d1:
            d1[j]=d1[j]+1
        else:
            d1[j]=1
    answer=int(list(d1.keys())[0])
    for j in d1:
        if d1[j]>d1[answer] and answer!=0:
            answer=j
        elif answer>j and d1[j]==d1[answer]:
            answer=j
    print(answer)
                
            
        


    
    '''
    help=[]
    another=[]
    for i in A:
        if i in another:
            pass
        else:
            help.append(A.count(i))
            another.append(i)
    
    answer=help[0]
    print(help,sep="")
    for i in help:
        temp=help.count(i)
        if help.count(answer)==temp and i<answer:
            answer=i
        elif temp>help.count(answer):
            answer=i
    print(answer)
            
    '''
            
            
        
