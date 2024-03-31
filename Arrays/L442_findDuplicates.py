#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
# Constraint : Time Complexity O(n) and Space Complexity O(1)

def findDuplicates(nums):
    res = []
    for i in nums:
        i = abs(i)
        if nums[i-1] < 0:
            res.append(i)
        nums[i-1] = -nums[i-1]
    return res

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))