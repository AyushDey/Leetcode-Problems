#Input: nums = [1,1,1,2,2,2,3], k = 2
#Output: [1,2]
#Input: nums = [1,2], k = 2
#Output: [1,2]

# Time complexity
# O(n log n) due to sorting the list of unique elements, where n is the number of unique elements in the input list.
from collections import Counter
# Time Complexity
def topKSorting(nums, k):
    common = Counter(nums).most_common(k)
    return [i[0] for i in common]

# Time Complexity
# O(n) using frequency maps to store the frequency of numbers in the array index
def toKFreqMap(nums, k):
    s = {}
    freq = [[] for i in range(len(nums) + 1)]
    for i in nums:
        s[i] = s.get(i, 0) + 1
    
    for key, val in s.items():
        freq[val].append(key)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

from collections import Counter            
def topKCounter(nums, k):
    count = Counter(nums)
    freq = [[] for i in range(len(nums) + 1)]

    for key, val in count.items():
        freq[val].append(key)
    
    res = []
    for n in reversed(freq):
        for num in n:
            res.append(num)
            if len(res) == k:
                return res


nums = [1,1,1,2,2,2,3]
k = 2
print(topKSorting(nums,k))
print(toKFreqMap(nums,k))
print(topKCounter(nums,k))