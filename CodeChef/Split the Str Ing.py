for _ in range(int(input())):
    N=int(input())
    S=str(input())
    print("YES" if S[-1] in S[:-1] else "NO")
    
