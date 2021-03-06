#1773. Count Items Matching a Rule
items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
indexget = dict()
indexget["type"] = 0
indexget["color"] = 1
indexget["name"] = 2
output = 0

for row in items:
    if row[indexget[ruleKey]] == ruleValue:
        output+=1
print(output)
