# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j
# such that nums[i] == nums[j] and abs(i - j) <= k.
# Example:
# Input: nums = [1,2,3,1], k = 3
# Output: true
def duplicates2(nums, k):
    hmap = {}
    for i, val in enumerate(nums):
        if val in hmap and abs(i - hmap[val]) <= k:
            return True
        hmap[val] = i
    return False

            

nums = list(map(int, input().strip().split()))
k = int(input())
print(duplicates2(nums, k))