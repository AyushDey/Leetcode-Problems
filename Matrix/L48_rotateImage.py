# Input:    ->    Output:
# [[1,2,3],       [[7,4,1], 
#  [4,5,6],  ->    [8,5,2],
#  [7,8,9]]        [9,6,3]]

def rotateMatrixRight(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()


matrix = [[1,2,3], [4,5,6], [7,8,9]]
rotateMatrixRight(matrix)
print(matrix)