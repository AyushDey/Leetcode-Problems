#Input: nums = [1,1,1,2,2,3]
#Output: 5, nums = [1,1,2,2,3,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).
from collections import Counter
def removeDuplicates2(nums):
    a = Counter(nums)
    for key, val in a.items():
        while val > 2:
            nums.remove(key)
            val -= 1
    return nums
    

nums = [1,1,1,2,2,3]
print(removeDuplicates2(nums))
print(removeDup(nums))