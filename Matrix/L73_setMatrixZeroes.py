# Input: matrix = 
# [[0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]]
# Output: 
# [[0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]]

def setMatrixwithMemory(matrix):
    row, col = [1]*len(matrix), [1]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if row[i] == 0 or col[j] == 0:
                matrix[i][j] = 0
            
    return matrix



matrix = [[1,1,1],[1,0,1],[1,1,1]]


print(setMatrixwithMemory(matrix))
