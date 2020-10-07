#Count pairs with given sum
sum=int(input())
count=0
lst=list(map(int,input().split()))
for i in range(len(lst)):
    for j in range(i,len(lst)):
        if lst[i]+lst[j]==sum:
            count+=1
            print(lst[i],lst[j],sep=" ")

print("count=",count)
