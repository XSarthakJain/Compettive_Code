#Bubble Sort
'''Worst Time Complexity & Average = O(n2)
Best Time Complexity=O(n)
Auxilary Space Complexity=O(1)'''
n=list(map(int,input().split()))

for i in range(len(n)):
    swapped=False
    for j in range(0,len(n)-i-1):
        if n[j]>n[j+1]:
            n[j+1],n[j]=n[j],n[j+1]
            swapped=True
    if swapped == False:
        print("Run Break")
        break

print("Sorted List = ",n)
    
