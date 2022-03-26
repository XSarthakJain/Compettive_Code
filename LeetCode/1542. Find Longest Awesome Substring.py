#1542. Find Longest Awesome Substring
s = "9498331"
result = 0
occurance = {}
for i in s:
    if i not in occurance:
        occurance[i] = 1
    else:
        occurance[i]+=1

for item in occurance:
    result+=occurance[item]//2
result = result*2
if len(s)> result:
    result+=1
print("Result = ",result)


    
