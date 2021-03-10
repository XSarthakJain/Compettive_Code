#1768. Merge Strings Alternately
words1 = "abbd"
words2 = "pqrs"
output = []

for i in range(min(len(words1),len(words2))):
    output.append(words1[i])
    output.append(words2[i])
if len(words1) > len(words2):
    output.append(words1[len(words2):])
else:
    output.append(words2[len(words1):])
print("".join(output))
