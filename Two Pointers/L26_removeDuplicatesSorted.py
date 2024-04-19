# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, 
# with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the 
# returned k (hence they are underscores).

def removeDuplicatesSorted(nums):
    count = 0
    last = None
    for i in nums:
        if i == last : continue
        last = i
        nums[count] = i
        count += 1
    return count

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicatesSorted(nums))