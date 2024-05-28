# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.

def maxFrequency(nums, k):
    nums.sort()
    l = r = count = 0
    n = len(nums)
    while r < n:
        count += nums[r]
        # Sum of elements till r < Sum if all elements till index r were same as nums[r]
        if count + k < nums[r] * (r - l + 1):
            count -= nums[l]
            l += 1
        r += 1
    return r - l



nums = list(map(int, input().split()))
k = int(input())
print(maxFrequency(nums, k))