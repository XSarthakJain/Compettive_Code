#1078. Occurrences After Bigram
text = "alice is a good girl she is a good student"; first = "a"; second = "good"
result = []
text = list(text.split())
for i in range(0,len(text)-2):
    print(text[i])
    if text[i] == first and text[i+1] == second:
        result.append(text[i+2])
    
        
print(result)
