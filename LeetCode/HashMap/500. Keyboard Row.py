#500. Keyboard Row
words = ["Hello", "Alaska", "Dad", "Peace"]
first_row = ['q','w','e','r','t','y','u','i','o','p']
second_row = ['a','s','d','f','g','h','j','k','l']
third_row = ['z','x','c','v','b','n','m']
result = []
for i in words:
    row = []
    curr = i
    i = i.lower()
    if i[0] in first_row:
        row = first_row
    elif i[0] in second_row:
        row = second_row
    elif i[0] in third_row:
        row = third_row
    flag = True
    
    for j in i:
        if j not in row:
            flag = False
            break
    if flag:
        result.append(curr)
print(result)
    
