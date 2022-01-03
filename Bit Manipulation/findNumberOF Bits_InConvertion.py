element1 = 13
element2 = 5

#XOR
mask = element1 ^ element2
#Count Number OF Ones
count = 0
while(mask):
    count+=1
    mask = (mask&(mask-1))
print("Count =",count)
