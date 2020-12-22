#1450. Number of Students Doing Homework at a Given Time
startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
result=0
for i in range(len(startTime)):
    if startTime[i]<=queryTime and endTime[i]>=queryTime:
        result+=1
print(result)
