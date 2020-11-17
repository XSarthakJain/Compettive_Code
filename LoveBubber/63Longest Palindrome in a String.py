for _ in range(int(input())):
    S=input()
    l=S[0]
    for i in range(len(S)):
       for j in range(len(S)-1,i,-1):
           #print(S[i],S[j])
           if S[i]==S[j]:
               #print(S[i:j+1],S[j:i-1:-1])
               if S[i:j+1]==S[j:i-1:-1]: 
                   l=max(S[i:j+1],l,key=len)
    print(l)
