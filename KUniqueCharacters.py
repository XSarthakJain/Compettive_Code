#KUniqueCharacters

s=input()
ans=""
for i in range(1,len(s)):
    for j in range(i,len(s)):
        if (len(ans)<len(s[i:j+1])) and (int(s[0])>=len(set(list(s[i:j+1])))):
            ans=s[i:j+1]
print(ans)










