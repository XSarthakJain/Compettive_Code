A=input()
help=list(set(A.split(" ")))

for i in help:
    if A.count(i)>1:
        print(i,A.count(i),sep=" ")
    
