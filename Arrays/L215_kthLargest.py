# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Explanation: Given an integer array nums and an integer k, 
# return the kth largest element in the array without sorting it.

def kthLargest(nums, k):
    maxel = 0
    for i in range(k):
        mxi = nums.index(max(nums))
        maxel = nums.pop(mxi)
    return maxel

nums = list(map(int, input().strip().split()))
k = int(input())
print(kthLargest(nums, k))