# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Explanation:
# 1 -> 2 -> 3
#           |
# 8 -> 9 -> 4
# |         |
# 7 <- 6 <- 5

def genSpiral(n):
    k = 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    result = []

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(k)
            k += 1
        top += 1
        for i in range(top, bottom + 1):
            


n = 3
print(genSpiral(n))