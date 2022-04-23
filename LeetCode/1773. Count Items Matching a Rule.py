#1773. Count Items Matching a Rule
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

resultCount = 0
for i in items:
    if ruleKey == "type":
        if i[0] == ruleValue:
            resultCount+=1
    elif ruleKey == "color":
        if i[1] == ruleValue:
            resultCount+=1
    else:
        if i[2] == ruleValue:
            resultCount+=1
print("Total Match Value = ",resultCount)
