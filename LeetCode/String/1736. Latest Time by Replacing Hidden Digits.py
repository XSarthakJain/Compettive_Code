#1736. Latest Time by Replacing Hidden Digits
time1 = "1?:22"
time = []
for i in time1:
    time.append(i)
print(time)
if time[0] == "?":
    if time[1] == "?":
        time[0] = "2"
    elif int(time[1]) > 3:
        time[0] = "1"
    else:
        time[0] = "2"
if time[1] == "?":
    if int(time[0]) < 2:
        time[1] = "9"
    else:
        time[1] = "3"
        
if time[3] == "?":
    if time[4] == "?":
        time[3] = "5"
if time[4] == "?":
    time[4] = "9"
    
        

print("".join(time))
    
