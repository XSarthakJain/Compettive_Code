#1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

arr = [1,1,1,1,1]
k = 1
threshold = 0
total = 0
c=0
window=0
for i in range(len(arr)):
    if (i-window)<k-1:
        total+=arr[i]
    else:
        total+=arr[i]
        if (total//k)>=threshold:
            c+=1
        total=total-arr[window]
        window+=1
print(c)
            
        
    


