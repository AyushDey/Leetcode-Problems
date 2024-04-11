# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

import sys
def maxSubArray(nums):
    maxi = -sys.maxsize - 1
    sum = 0
    for i in range(len(nums)):
        sum+= nums[i]

        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))