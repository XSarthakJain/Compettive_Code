#2273. Find Resultant Array After Removing Anagrams
words = ["abba","baba","bbaa","cd","cd"]
pointer = 0
for index,item in enumerate(words):
    if index>0:
        if "".join(sorted(item)) == "".join(sorted(words[pointer])):
            words[index] = "@"
        else:
            pointer = index
print([i for i in words if i!="@"])
            
            
        
        
        
        
    
