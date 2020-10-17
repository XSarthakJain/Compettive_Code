# cook your dish here
for _ in range(int(input())):
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    result=-1
    resulted_Item=-1
    for i in range(N):
        if i==P[i]-1:
            if K%P[i]==0:
                if result>K//P[i]:
                    result=K//P[i]
                    resulted_Item=P[i]
        else:
            if K%P[i]==0:
                print("VAlues",P[i])
                if result==-1:
                    result=(K//P[i])+1
                    resulted_Item=P[i]
                elif result>(K//P[i])+1:
                    result=(K//P[i])+1
                    resulted_Item=P[i]
    print(resulted_Item)
            





'''
    result=0
    resulted_Item=-1
    for i in range(N):
        if i+1==(P[i]):
            if K%P[i]==0 and result>K//P[i]:
                resulted_Item=P[i]
                result=K//P[i]
        else:
            if K%P[i]==0 and result>((K//P[i])+1):
                resulted_Item=P[i]
                result=(K//P[i])+1
    print(resulted_Item)
            
                

'''
