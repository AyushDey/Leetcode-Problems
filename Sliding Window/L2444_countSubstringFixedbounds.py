#Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
#Output: 2
#Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

def countSubstringFixedbounds(nums, minK, maxK):
    res = 0
    bad_idx = min_idx = max_idx = -1
    for i, val in enumerate(nums):
        if not minK <= val <= maxK:
            bad_idx = i
        if val == minK:
            min_idx = i
        if val == maxK:
            max_idx = i
        res += max(0, min(min_idx, max_idx) - bad_idx)
    return res


nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
print(countSubstringFixedbounds(nums, minK, maxK))