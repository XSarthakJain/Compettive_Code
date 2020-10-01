#Selection Sort
'''
Auxilary Space Complexity O(1)
Time Complexity=O(n2)
'''

n=list(map(int,input().split()))

for i in range(len(n)):
    min=i
    for j in range(i+1,len(n)):
        if n[min]>n[j]:
            min=j

    n[min],n[i]=n[i],n[min]
print("Sorted Array = ",n)
    
