# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 1 -> 2 -> 3
#           |
# 4 -> 5 -> 6
# |         |
# 7 <- 8 <- 9

# Time complexity: O(n)
# Space complexity: O(1)

def spiralMatrix(matrix):
    if not matrix: return []
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    row, col = len(matrix), len(matrix[0])
    while top <= bottom and left <= right:
        # Top row
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        # Right column
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        # Bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
        # Left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


#matrix = [[int(x) for x in input().split()] for _ in range(int(input("Enter the number of rows: ")))]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))