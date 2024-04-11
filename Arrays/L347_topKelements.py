#Input: nums = [1,1,1,2,2,2,3], k = 2
#Output: [1,2]
#Input: nums = [1,2], k = 2
#Output: [1,2]
from collections import Counter
def topK(nums, k):
    nums1 = Counter(nums)
    common = Counter(nums).most_common(k)
    return [i[0] for i in common]

nums = [1,1,1,2,2,2,3]
k = 2
print(topK(nums,k))