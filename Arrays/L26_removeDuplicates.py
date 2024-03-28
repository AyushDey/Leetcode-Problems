from collections import Counter
def remove_duplicates(nums):
    unique_nums = set()
    i = 0
    while i < len(nums):
        if nums[i] in unique_nums:
            nums.pop(i)
        else:
            unique_nums.add(nums[i])
            i += 1
    return len(nums)
def removeDuplicates(nums):
        counter = Counter(nums)
        for num, val in counter.items():
            while val > 1:
                nums.remove(num)
                val -= 1
nums = [0,0,1,1,1,2,2,3,3,4]
#print(remove_duplicates(nums))
removeDuplicates(nums)
print(nums)