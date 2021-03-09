#1408. String Matching in an Array
words = ["mass","as","hero","superhero"]
output = []
#sort by length
words.sort(key=len)
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i] in words[j]:
            output.append(words[i])
            break
print(output)

