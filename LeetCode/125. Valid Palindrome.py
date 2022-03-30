#125. Valid Palindrome
s = "A man, a plan, a canal: Panama"
result = ""
s = s.replace(" ","")
s = s.lower()
for i in s:
    if i.isalnum():
        result+=i
print("Result = ",(result==result[-1::-1]))
        
