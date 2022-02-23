n = list(input())
pivot = len(n)-1
for index,item in enumerate(reversed(n)):
    if n[len(n)-1-index] < n[pivot]:
        n[len(n)-1-index],n[pivot] = n[pivot],n[len(n)-1-index]
        break
print("".join(n))
