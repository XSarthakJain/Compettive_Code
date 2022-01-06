n = int(input())
proResult = 1
sumResult = 0

while(True):
    modular = n%10
    print("Modular",modular)
    proResult *=modular
    sumResult+=modular

    n=n//10
    if(n<1):
        break
print("Result =",proResult - sumResult)
