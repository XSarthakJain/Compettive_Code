#1678. Goal Parser Interpretation
command = "(al)G(al)()()G"
output = []
for i in range(len(command)):
    if command[i] == "(":
        if command[i+1] == ")":
            output.append("o")
    elif command[i] == ")":
        pass
    else:
        output.append(command[i])
print("".join(output))
    
