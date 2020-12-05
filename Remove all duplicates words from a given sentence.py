#Python | Remove all duplicates words from a given sentence
s=list(input().split())
d=dict()
for i in s:
    if i not in d:
        d[i]=i
        print(i,end=" ")
