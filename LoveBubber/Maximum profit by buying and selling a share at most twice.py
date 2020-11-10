N=list(map(int,input().split()))
min=N[0]
profit=N[1]-N[0] if N[1]>N[0] else 0
all_profit=0
for i in range(1,len(N)):
    if min>N[i]:
        min=N [i]
        all_profit+=profit
    else:
        profit=N[i]-min
print(all_profit)
