# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

def moveZeroes(nums):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1
    nums[k:] = [0 for i in range(n-k)]

nums = list(map(int, input().split()))
moveZeroes(nums)
print(nums)