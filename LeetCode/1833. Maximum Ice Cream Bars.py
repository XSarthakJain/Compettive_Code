#1833. Maximum Ice Cream Bars
costs = [1,3,2,4,1]
coins = 7
costs.sort()
result = 0
for i in costs:
    if i<=coins:
        result+=1
        coins-=i
print(result)
