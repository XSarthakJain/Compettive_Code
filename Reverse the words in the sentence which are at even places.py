#Reverse Word
A = input()
A = A.split(" ")
result = []
even =[]
odd= []
for i in range(len(A)):
    if i%2!=0:
        even.append(A[i])
    else:
        odd.append(A[i])
even.reverse()
print("Reverse",even)
e=0
o=0
for i in range(len(A)):
    if i%2!=0:
        result.append(even[e])
        e+=1
    else:
        result.append(odd[o])
        o+=1

print(result)
