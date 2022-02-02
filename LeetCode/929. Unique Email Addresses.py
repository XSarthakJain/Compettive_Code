#929. Unique Email Addresses
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
result = set()
for i in emails:
    dummy = (i.split("@")[0]).replace(".","")
    dummyIndex = len(i)
    try:
        dummyIndex = dummy.index("+")
    except:
        pass
    result.add(dummy[0:dummyIndex]+"@"+(i.split("@")[1]))
print("Result = ",result,len(result))
    
    
    
