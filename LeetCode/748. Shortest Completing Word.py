#748. Shortest Completing Word
import re
licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
licensePlate = re.sub(r"[^a-z]","",licensePlate.lower())
result=""
for item in words:
    flag = True
    dummyItem = item
    for j in licensePlate:
        if j not in dummyItem:
            flag=False
            break
        dummyItem=dummyItem.replace(j,"",1)
    if flag:
        if result=="" or len(item)<len(result):
            result=item
print("Item",result)
