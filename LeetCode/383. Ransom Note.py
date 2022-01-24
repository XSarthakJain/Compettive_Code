#383. Ransom Note
ransomNote = "aa"
magazine = "aab"
ransomDict = {}
magazineDict = {}

for i in ransomNote:
    if i not in ransomDict:
        ransomDict[i] = 1
    else:
        ransomDict[i]+=1

for i in magazine:
    if i not in magazineDict:
        magazineDict[i] = 1
    else:
        magazineDict[i]+=1
flag = True
for i in ransomDict:
    if i in magazineDict and ransomDict[i]<=magazineDict[i]:
        pass
    else:
        flag=False
        break
print(flag)
    
