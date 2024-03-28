#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4

def searchRotated(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if target == nums[m]:
            return m
        # Left Sorted Portion 
        if nums[l] <= nums[m]:
            # [l, mid, target, r]
            if target > nums[m] or target < nums[l]:
                l = m + 1 # go left
            # [l, target, mid, r]
            else:
                r = m - 1 # search left
        # Right Sorted Position
        else:
            # [l, target, mid, r]
            if target < nums[m] or target > nums[r]:
                r = m - 1 # go left
            else:
            # [l, mid, target, r]
                l = m + 1 # search right
    return -1



nums = list(map(int, input().strip().split())) #[4,5,6,7,0,1,2]
target = 0
print(searchRotated(nums, target))
