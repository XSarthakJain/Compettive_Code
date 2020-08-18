t=int(input())
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split()))
    Esum=0
    Osum=0
    flag=0
    if len(ai)>2:
        for j in range(2,len(ai)):
            if flag==0:
                Esum=ai[j]
                flag=1
            else:
                Osum=ai[j]
                flag=0
        Esum=Esum+ai[1]
        Osum=Osum+ai[0]
        if Esum>Osum:
            print("second")
        elif Osum>Esum:
            print("first")
        else:
            print("draw")
            
    else:
        if a[0]>a[1]:
            print("first")
        elif a[1]>a[0]:
            print("second")
        else:
            print("draw")
        
      
