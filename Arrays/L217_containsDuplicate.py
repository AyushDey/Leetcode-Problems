#Input: nums = [1,2,3,1]
#Output: true

def containsDuplicate(nums):
    elements = set()
    for i in nums:
        if i in elements:
            return True
        elements.add(i)
    return False

nums = list(map(int, input().strip().split()))
print(containsDuplicate(nums))