#937. Reorder Data in Log Files
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
letter_logs = []
digit_logs = []

for i in logs:
    if i[-1].isalpha():
        dummy = []
        dummy.append(i[0:i.index(" ")])
        dummy.append(i[i.index(" ")+1:len(i)])
        letter_logs.append(dummy)
    else:
        digit_logs.append(i)
sorted_list = sorted(letter_logs,key=lambda x:(x[1],x[0]))
result = []
for i in sorted_list:
    result.append(i[0]+" "+i[1])
for i in digit_logs:
    result.append(i)
print("Result =",result)
