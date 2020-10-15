# cook your dish here
T=int(input())
for _ in range(T):
    H,P=map(int,input().split())
    while(True):
        H=H-P
        if P<1:
            print("0")
            break
        elif H<1:
            print("1")
            break
        P=P//2
