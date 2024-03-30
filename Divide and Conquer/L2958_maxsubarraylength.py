#Input: nums = [1,2,3,1,2,3,1,2], k = 2
#Output: 6
#Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
#It can be shown that there are no good subarrays with length more than 6.

# Sliding Window Approach Used
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
def maxsubarraylength(nums, k):
    count = defaultdict(int) # It means if new key is encountered value will be initialised with 0 
    max_len = 0 
    l = 0 
    for r in range(len(nums)): # r is the right pointer
        count[nums[r]] += 1 # increment the count of the current element
        while count[nums[r]] > k: # if the count of the current element is greater than k
            count[nums[l]] -= 1 # decrement the count of the left pointer element
            l += 1 # move the left pointer to the right
        max_len = max(max_len, r - l + 1) # update the max length
    return max_len

nums = [1,2,3,1,2,3,1,2]
k = 2
print(maxsubarraylength(nums,k))