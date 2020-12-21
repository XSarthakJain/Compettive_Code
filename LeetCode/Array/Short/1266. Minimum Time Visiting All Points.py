#1266. Minimum Time Visiting All Points
points = [[3,2],[-2,2]]
total_distance=0
for i in range(1,len(points)):
    x_distance=abs(points[i][0]-points[i-1][0])
    y_distance=abs(points[i][1]-points[i-1][1])
    total_distance+=max(x_distance,y_distance)
print("Minimum Distance ",total_distance)
