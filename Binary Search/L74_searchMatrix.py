#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true

def searchMatrix(matrix, target):
    for i in matrix:
        l, r = 0, len(i) - 1
        while l <= r: # Performs binary search in a row
            m = (l+r)//2
            if i[m] == target:
                return True
            elif i[m] > target:
                r = m - 1
            else:
                l = m + 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))