
def SearchElement():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target=3
    flag=True
    if len(matrix[0])>0:
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][(len(matrix[i]))-1]>=target:
                for j in range(len(matrix[0])):
                    if matrix[i][j]==target:
                        flag=False
                        return True
                    
    if flag:
        return False
                
print(SearchElement())


#LeetCode Solution https://leetcode.com/problems/search-a-2d-matrix/submissions/
