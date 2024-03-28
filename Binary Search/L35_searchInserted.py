#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2

#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1

def searchInserted(nums, target):
    l, r = 0, len(nums) - 1 
    while l <= r: 
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l # Because L points to the element position smaller than 
    #the number to be found which is equal to the position it should be if present

nums = list(map(int, input().strip().split()))
target = int(input())
print(searchInserted(nums, target))