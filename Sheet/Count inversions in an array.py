#Count inversions in an array
n = 5
arr = [1,20,6,4,5]

def Merge(arr,temp,left,mid,right):
    i = left
    j = mid+1
    k = left
    result = 0
    while(i<=mid and j<=right):
        if arr[i] > arr[j]:
            print(arr[i],arr[j],mid,i)
            temp[k] = arr[j]
            result += mid-i+1
            j+=1
        else:
            temp[k] = arr[i]
            i+=1
        k+=1
    while(i<=mid):
        temp[k] = arr[i]
        i+=1
        k+=1
    while(j<=right):
        temp[k] = arr[j]
        j+=1
        k+=1
    for i in range(left,right+1):
        arr[i] = temp[i]
    return result

def MergeSort(arr,temp,left,right):
    result = 0
    if left<right:
        mid = (left+right)//2
        result += MergeSort(arr,temp,left,mid)
        result += MergeSort(arr,temp,mid+1,right)
        result+= Merge(arr,temp,left,mid,right)
    return result
        
            
            
                
             
'''
for i in range(n):
    for j in range(n):
        if j>i and arr[i]>arr[j]:
            result+=1
'''
temp = [0]*len(arr)
    
print(MergeSort(arr,temp,0,len(arr)-1))
