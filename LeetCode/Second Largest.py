#Second MAximum Element
A=[3,7,5,76,3,34334,9]
first = A[0]
second = A[0]

for i in A:
    if i>first:
        first,second = i,first
print("first,second",first,second,sep=" ")
