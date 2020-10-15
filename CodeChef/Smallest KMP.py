#Smaller KMP
# cook your dish here
for _ in range(int(input())):
    T=list(input())
    s=input()
    for i in s:
        T.remove(i)
    T.append(s)
    T=sorted(T)
    print(*T,sep='')

