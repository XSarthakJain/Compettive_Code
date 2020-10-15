# cook your dish here
def check_For_L(k,N,counter):
   
    if counter&1: 
        if  matrix[0][k]!=(0)*N+(k+1):
            return False
    else:
        if matrix[k][0]!=(0)*N+(k+1):
            return False
        
    return True

T=int(input())
for _ in range(T):
    N=int(input())
    matrix=[]
    for j in range(N):
        matrix.append(list(map(int,input().split())))
    counter=0
    
    for j in reversed(range(N)):
        if check_For_L(j-1,N,counter):
            continue
        else:
            counter+=1
    
    print(counter)
            
