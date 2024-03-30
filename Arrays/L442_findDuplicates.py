#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
# Constraint : Time Complexity O(n) and Space Complexity O(1)

from collections import Counter
def findDuplicates(nums):
    visited = set()
    res = []
    for i in nums:
        if i in visited:
            res.append(i)
        else:
            visited.add(i)
    return res

def findDuplicates2(nums):
    return [key for key, value in Counter(nums).items() if value > 1]


nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
print(findDuplicates2(nums))