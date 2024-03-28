#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#Notice that the order of the output and the order of the triplets does not matter.

def threesum(nums):
    res = []
    nums.sort()
    for i, val in enumerate(nums):
        if i > 0 and val == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            tSum = val + nums[l] + nums[r]
            if tSum > 0:
                r -= 1
            elif tSum < 0:
                l += 1
            else:
                res.append([val, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res

nums = [-1,0,1,2,-1,-4]
print(threesum(nums))