#Input: matrix = [[1,2,3],[4,5,6]]
#Output: [[1,4],[2,5],[3,6]]
from numpy import transpose

def transposenormal(matrix):
    res = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        res.append(temp)
    return res

def transposezip(matrix):
    return list(zip(*matrix))



matrix = [[1,2,3],[4,5,6]]
print(transposezip(matrix))
print(transpose(matrix))
print(transposenormal(matrix))