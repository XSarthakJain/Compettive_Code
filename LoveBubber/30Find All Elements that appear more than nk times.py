#https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/
#Find All Elements that appear more than n/k times
n=list(map(int,input().split()))
K=int(input())
result=dict()
for i in n:
    if i in result:
        result[i]=result[i]+1
    else:
        result[i]=1

#Result
for i in result:
    if result[i]>(len(n)//K):
        print(i)
