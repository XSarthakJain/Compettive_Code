#Find Maximum & Minimum in Array
A=list(map(int,input().split()))
Max=A[0]
Min=A[0]
for i in range(len(A)):
    if Max<A[i]:
        Max=A[i]
    elif Min>A[i]:
        Min=A[i]
print("Max",Max)
print("Min",Min)
