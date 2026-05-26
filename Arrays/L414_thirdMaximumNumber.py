# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

from typing import List

class Solution:
    # Time Complexity
    # O(n log n) due to sorting the list of unique elements, where n is the number of unique elements in the input list.
    def thirdMaxBruteForce(self, nums: List[int]) -> int:
        nums_res = list(dict.fromkeys(nums))
        nums_res.sort(reverse=True)
        if len(nums_res) < 3:
            return nums_res[0]
        return nums_res[2]
    
    # Time Complexity
    # O(n)
    def thirdMax(self, nums: List[int]) -> int:  # noqa: F821
        first = second = third = float('-inf')
        for num in set(nums):
            if num > first:
                first, second, third = num, first, second
                # third = second
                # second = first
                # first = num
            elif num > second:
                second, third = num, second
                # third = second
                # second = num
            elif num > third:
                third = num
        
        return third if third != float('-inf') else first


# Add a main function
if __name__ == "__main__":
    solution = Solution()
    # print(solution.thirdMax([3, 2, 1]))  # Output: 1
    # print(solution.thirdMax([1, 2]))     # Output: 2
    print(solution.thirdMax([2, 2, 3, 1]))  # Output: 1