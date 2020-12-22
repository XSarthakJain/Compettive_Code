#1572. Matrix Diagonal Sum
mat = [[5]]

result=0
for first_diagonal in range(len(mat[0])):
    result+=mat[first_diagonal][first_diagonal]

    if first_diagonal!=len(mat)-first_diagonal-1:
        result+=mat[first_diagonal][len(mat)-first_diagonal-1]

print(result)
