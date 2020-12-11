#Check if a number is Palindrome
def palindrome(n,low,high):
    if low==high:
        return True
    else:
        return ((palindrome(n,low+1,high-1))if n[low]==n[high] else (False))

n=input()
print(palindrome(n,0,len(n)-1))
