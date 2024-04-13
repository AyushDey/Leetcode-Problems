# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sortColorsBucketSort(nums):
    num0 = num1 = num2 = 0
    for i in nums:
        if i == 0:
            num0 += 1
        elif i == 1:
            num1 += 1
        else:
            num2 += 1
    for i in range(num0):
        nums[i] = 0
    for i in range(num0, num0 + num1):
        nums[i] = 1
    for i in range(num0 + num1, num0 + num1 + num2):
        nums[i] = 2

def sortColors(nums):
    l, r = 0, len(nums) - 1
    i = 0        
    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
            i -= 1
        i += 1

nums = [2,0,2,1,1,0]
#sortColorsBucketSort(nums)
sortColors(nums)
print(nums)