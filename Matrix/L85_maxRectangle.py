#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 6
#Explanation: The maximal rectangle is shown in the above picture.


def maxRectangle(matrix):
    if not matrix:
        return 0
    row, col = len(matrix), len(matrix[0])
    height = [0] * (col + 1)
    maxArea = 0
    for row in matrix:
        for i in range(col):
            height[i] = height[i] + 1 if row[i] == "1" else 0
        stack = []
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(i)
    return maxArea

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maxRectangle(matrix))