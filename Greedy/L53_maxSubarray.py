# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(nums):
    maxi = -float('inf')
    currentsum = 0
    for i in range(len(nums)):
        currentsum+= nums[i]
        maxi = max(maxi, currentsum)
        currentsum = max(0, currentsum)
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))