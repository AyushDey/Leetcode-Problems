# Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
# Return the selected integer.
# Example 1:

# Input: nums = [3,2,1,4]
# Output: 2
# Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.
# Example 2:

# Input: nums = [1,2]
# Output: -1
# Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.

class Solution:
    # Time Complexity: O(n)
    def findNonMinOrMaxBruteForce(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1
        
        max_val = next_max_val = float('-inf')
        for num in set(nums):
            if num > max_val:
                max_val, next_max_val = num, max_val
            elif num > next_max_val:
                next_max_val = num

        return next_max_val
    
    # Time Complexity : O(1)
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return -1
        
        a, b, c = nums[0], nums[1], nums[2]
        min = max = a
        if b < min:
            min = b
        if b > max:
            max = b
        if c < min:
            min = c
        if c > max:
            max = c
        
        if a != min and a != max:
            return a
        if b != min and b != max:
            return b
        else:
            return c
        
        


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNonMinOrMax([3, 2, 1]))  # Output: 2
    print(solution.findNonMinOrMax([1, 2]))     # Output: -1
    print(solution.findNonMinOrMax([2, 2, 3, 1]))  # Output: 2