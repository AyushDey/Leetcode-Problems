#Input: nums = [1,2,1,2,3], k = 2
#Output: 7
#Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# https://youtu.be/etI6HqWVa8U?si=AaJPLorvLcE3pLR3
from collections import defaultdict
def subarrayWithKDistinct(nums, k):
    count = defaultdict(int)
    res = l_near = l_far = 0
    for r in range(len(nums)):
        count[nums[r]] += 1

        while len(count) > k:
            count[nums[l_near]] -= 1
            if count[nums[l_near]] == 0:
                count.pop(nums[l_near])
            l_near += 1
            l_far = l_near
        while count[nums[l_near]] > 1:
            count[nums[l_near]] -= 1
            l_near += 1

        if len(count) == k:
            res += l_near - l_far + 1
    return res 

nums = [1,2,1,2,3]
k = 2
print(subarrayWithKDistinct(nums, k))