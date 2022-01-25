#345. Reverse Vowels of a String
s="leetcode"
temp = s
s=[]
s[:0] = temp
leftIndex = 0
rightIndex = len(s)-1
vowels = ['a','e','i','o','u']
while(leftIndex<rightIndex):
    if s[leftIndex].lower() in vowels:
        if s[rightIndex].lower() in vowels:
            s[leftIndex],s[rightIndex] = s[rightIndex],s[leftIndex]
            leftIndex+=1
            rightIndex-=1
        else:
            rightIndex-=1
    elif s[rightIndex].lower() in vowels:
        leftIndex+=1
    else:
        leftIndex+=1
        rightIndex-=1
print("Reverse String = ","".join(s))
        
        
