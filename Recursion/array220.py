#array220
'''
Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.


array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
'''

def array220(n,l):
    if len(n)==l+1:
        return (True if n[l]%10==0 else False)
    else:
        return (True if n[l]%10==0 else array220(n,l+1))


n=list(map(int,input().split()))
print(array220(n,0))
