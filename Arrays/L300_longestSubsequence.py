'''Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''
#Using Greedy and Binary Search
def longestSubsequence(nums):
    res = []
    
    def binarySearch(res, num):
        low, high = 0, len(res)
        while low < high:
            mid = (low + high) // 2
            if res[mid] < num:
                low = mid + 1
            else:
                high = mid
        return low
    
    for num in nums:
        pos = binarySearch(res,num)
        if pos == len(res):
            res.append(num)
        else:
            res[pos] = num

    return len(res)

def longestSubsequenceDP(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(0,i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) 

nums = list(map(int, input().split()))
print(longestSubsequence(nums))
#print(longestSubsequenceDP(nums))