# Input: nums = [4,1,2,1,2]
# Output: 4
# Explanation:
# XOR of two same numbers is always 0 i.e. a ^ a = 0.
# XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.

# Assume the given array is: [4,1,2,1,2]
# XOR of all elements = 4^1^2^1^2
#      = 4 ^ (1^1) ^ (2^2)
#      = 4 ^ 0 ^ 0 = 4^0 = 4
# Hence, 4 is the single element in the array.

def singlenum(nums):
    res = 0
    for i in nums:
        res ^= i
    return res



nums = [4,1,2,1,2]
print(singlenum(nums))