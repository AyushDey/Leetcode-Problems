#Input: nums = [1,1,1,2,2,3]
#Output: 5, nums = [1,1,2,2,3,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).
def removeDuplicates2(nums):
    ind = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[ind - 2]:
            nums[ind] = nums[i]
            ind += 1
    return ind
    

nums = [1,1,1,2,2,3]
print(removeDuplicates2(nums))
