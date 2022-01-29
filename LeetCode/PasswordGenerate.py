pass_length = int(input("Password Length :"))
upperCase_length = int(input("UpperCase Length :"))
digit_length = int(input("Digit Length :"))
symbol_length = int(input("Symbol Length :"))
import random
import string
result = ""
result = "".join(random.choice(string.ascii_uppercase) for _ in range(upperCase_length))
result += "".join(random.choice(string.digits) for _ in range(digit_length))
result += "".join(random.choice(string.punctuation) for _ in range(symbol_length))
if len(result)!=pass_length:
    result += "".join(random.choice(result) for _ in range(pass_length-len(result)))
print(result)
