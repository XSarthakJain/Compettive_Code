#1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
sentence = "i love eating burger"
searchWord = "burg"
result = -1
sentence = sentence.split(" ")
for i in range(len(sentence)):
    if sentence[i][:len(searchWord)] == searchWord:
        result = i+1
        break
print(result)
