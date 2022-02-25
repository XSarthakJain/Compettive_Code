#804. Unique Morse Code Words
morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin","zen","gig","msg"]
result = set()
for i in words:
    tempResult = ""
    for j in i:
        tempResult+=morseCode[int(ord(j))-97]
    result.add(tempResult)
print("Result = ",len(result),result,morseCode[6])
