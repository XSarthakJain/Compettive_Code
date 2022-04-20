#1598. Crawler Log Folder
logs = ["./","../","./"]
result = 0
for i in logs:
    if i == "../" and result!=0:
        result-=1
    elif i == "./":
        pass
    elif i!="../":
        result+=1
    print(i,result)
print("Result = ",result)
