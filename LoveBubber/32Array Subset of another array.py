#code
for _ in range(int(input())):
    m,n=map(int,input().split())
    arr1=set(map(int,input().split()))
    arr2=set(map(int,input().split()))
    print("Yes" if arr2.issubset(arr1) else "No")
