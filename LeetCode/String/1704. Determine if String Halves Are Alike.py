#1704. Determine if String Halves Are Alike
s = "textbook"
s = s.lower()
vowel = ["a","e","i","o","u"]
left = 0
right = 0
for i in range(len(s)//2):
    if s[i] in vowel:
        left+=1
for i in range((len(s)+1)//2,len(s):
    if s[i] in vowel:
        right+=1
        print(s[i])
print(left,right)

if left == right:
    print(True)
else:
    print(False)
