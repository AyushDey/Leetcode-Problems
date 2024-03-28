#Input: nums = [3,2,4], target = 6
#Output: [1,2]

def twosum(nums, target):
    # Dictionary to store numbers and positions
    ar = {}
    val = 0
    for i in range(len(nums)):
        val = target - nums[i]
        if val in ar:
            return [ar[val], i]
            
        ar[nums[i]] = i 

nums = list(map(int, input().strip().split()))
target = int(input())
print(twosum(nums, target))
