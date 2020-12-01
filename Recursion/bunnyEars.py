#bunnyEars
'''
We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
'''
def bunnies(n):
    if n==0:
        return 0
    else:
        return 2+(bunnies(n-1))
n=int(input())
print(bunnies(n))
