#count7
'''
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


count7(717) → 2
count7(7) → 1
count7(123) → 0
'''

def count7(n):
    if n//10==0:
        return (1 if n==7 else 0)
    elif n%10==7:
        return 1+(count7(n//10))
    else:
        return count7(n//10)
        


n=int(input())
print(count7(n))
