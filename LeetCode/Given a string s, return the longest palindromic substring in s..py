s = "cbbd"
total = s[0] if s else ""
for index,item in enumerate(s):
    for j in range(len(s),index,-1):
        temp = index-1 if index != 0 else None
        print(s[index:j:1] , s[j-1:temp:-1],j-1,temp)
        if s[index:j:1] == s[j-1:temp:-1]:
            total = s[index:j] if len(s[index:j]) > len(total) else total
print(total)
            
        
