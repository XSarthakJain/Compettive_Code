#Cyclically rotate an array by one / Right Rotation
A=list(map(int,input().split()))
rotate=1#Number Of Cylinder Rotation
print(*A[(len(A)-rotate):],*A[0:len(A)-rotate],sep="")
