#Input: nums = [3,1,4,1,5], k = 2
#Output: 2
#Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
#Although we have two 1s in the input, we should only return the number of 
# unique pairs.

from collections import Counter
def k_diff(nums, k):
    c_nums = Counter(nums) # [(num, freq)]
    c = 0
    if k == 0:
        for key, val in c_nums.items(): # key = element, val = freq
            if val > 1: #if k = 0, find if there are multiple values in nums 
                c += 1
    else:
        for key, val in c_nums.items(): 
            if key+k in c_nums: # e.g [3,1,4,1,5], if 1+2 = 3 which is present in 
                c += 1
    return c


nums = list(map(int, input().strip().split()))
k = int(input())
print(k_diff(nums,k))
