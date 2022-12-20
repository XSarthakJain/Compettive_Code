#56. Merge Intervals
intervals = [[1,3],[2,6],[8,10],[15,18]]
result = []
intervals.sort(key=lambda x:x[0])
beg = intervals[0][0]
end = intervals[0][1]
for i in range(len(intervals)):
    
    if i!=0 and end < intervals[i][0]:
        result.append([beg,max(intervals[i-1][1],end)])
        beg = intervals[i][0]
        end = intervals[i][1]
    else:
        end = max(intervals[i][1],end)
result.append([beg,end]) 
print(result)
