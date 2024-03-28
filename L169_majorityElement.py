#Input: nums = [3,2,3]
#Output: 3
from collections import Counter
def majority(nums):
    a = Counter(nums)
    return a.most_common(1)[0][0]  #most_common(1) returns a list of tuples, so we take the first tuple and return the first element of that tuple. 

nums = list(map(int, input().strip().split()))
print(majority(nums))