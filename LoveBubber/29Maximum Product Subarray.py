#Maximum Product Subarray
#Help https://youtu.be/vtJvbRlHqTA

arr=list(map(int,input().split()))
prev_max=arr[0]
prev_min=arr[0]
ans=arr[0]
for i in range(1,len(arr)):
    current_max=max(prev_max*arr[i],arr[i],prev_min*arr[i],arr[i])
    current_min=min(prev_max*arr[i],prev_min*arr[i],i)
    ans=max(ans,current_max)
    prev_max=current_max
    prev_min=current_min
print(ans)
