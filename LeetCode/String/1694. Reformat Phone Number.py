#1694. Reformat Phone Number
number_input = "--17-5 229 35-39475"
number_input1 = "".join((number_input.split(" ")))
number = "".join(number_input1.split("-"))
print(number)
output = []
if len(number)%3 == 1:
    ren = (len(number)//3) - 1    
else:
    ren = (len(number)//3)
ptr = 0
for i in range(ren):
    output.append(number[ptr])
    ptr+=1
    output.append(number[ptr])
    ptr+=1
    output.append(number[ptr])
    ptr+=1
    output.append("-")
r = ((len(number)%3 +1) if len(number)%3!=0 else len(number)%3)
print(r,output)
for j in range((len(number)-ptr)//2):
    output.append(number[ptr]) 
    ptr +=1
    if ptr < len(number):
        output.append(number[ptr])
        ptr += 1
        output.append("-")
print("".join((output[:-1]) if output[-1] == "-" else (output)))
