#520. Detect Capital
word = "USA"
if word.upper() == word or word.lower() == word or (word[0]+word[1:].lower()) == word:
    return True
return False
