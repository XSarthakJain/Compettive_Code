#3. Longest Substring Without Repeating Characters
s = ""
store = set()
pointer = 0
total = 0
for index,item in enumerate(s):
    temp = pointer
    while(temp!= index):
        if item in store:
            store.remove(s[pointer])
            pointer+=1
        else:
            break
        temp+=1
    store.add(item)
    total = max(total,(index-pointer+1))
print(total)
        
                
   
        
