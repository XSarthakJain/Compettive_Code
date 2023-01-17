#1232. Check If It Is a Straight Line
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
def calculate(p1,p2):
    if p1[0] == p2[0]:#Prevent for divide by Zero 
        return 9999999999999
    result = (p2[1] - p1[1])/(p2[0]-p1[0])
    return result
slop = calculate(coordinates[0],coordinates[1])
for i in range(2,len(coordinates)):
    if slop!= calculate(coordinates[i-1],coordinates[i]):
        return False
return True

