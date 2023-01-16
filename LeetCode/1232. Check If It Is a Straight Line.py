#1232. Check If It Is a Straight Line
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
coordinates.sort(key=lambda x: (x[0], x[1]))
first = coordinates[-1][0] - coordinates[0][0]
second = coordinates[-1][1] - coordinates[0][1]
prev = coordinates[0]
for i in range(1,len(coordinates)):
    print(prev,coordinates[i])
    if first>0:
        coordinates[i][0] == prev[0]+1
    elif first<0:
        coordinates[i][0] == prev[0]-1
    else:
        print(False)

    if second>0:
        coordinates[i][1] == prev[1]+1
    elif second<0:
        coordinates[i][1] == prev[1]-1
    else:
        print(False)
    prev = coordinates[i]
print(True)
