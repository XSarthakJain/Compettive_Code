#3. Longest Substring Without Repeating Characters
s = "dvdf"
start = 0
end = 0
result =  0
dummyResult = 0
for index,item in enumerate(s):

    try:
        if s[start:end].find(item)>=0:
            result = max(result,dummyResult)
            dummyResult=1
            occuranceItem = s[start:end].index(item)
            start = start+occuranceItem+1
    except:
        pass
    dummyResult+=1
    print(start,end,s[start:end],item,dummyResult)
        
    
    end+=1
print("Result",max(result,dummyResult))
