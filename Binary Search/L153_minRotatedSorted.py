#Input: nums = [3,4,5,1,2]
#Output: 1
#Explanation: The original array was [1,2,3,4,5] rotated 3 times.

def minrotatedSorted(nums):
    l, r = 0, len(nums) - 1
    minval = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            minval = min(minval, nums[l])
            break
        m = (l+r)//2
        minval = min(minval,nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return minval


nums = list(map(int, input().strip().split()))
print(minrotatedSorted(nums))