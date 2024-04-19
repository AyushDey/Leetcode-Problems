#Input: nums = [1,1,2,3,3,4,4,8,8]
#Output: 2
# Explanation: 2 appears only once
# Time complexity: O(log n)
# Space complexity: O(1)

def singleElement(nums):
    # Initialize pointers to the start and end of the array
    l, r = 0, len(nums) - 1

    # While the left pointer is less than the right pointer
    while l < r:
        # Calculate the middle index
        mid = (l + r) // 2

        # If the element at the middle index is equal to the element at the bitwise XOR of the middle index and 1
        if nums[mid] == nums[mid ^ 1]:
            # Move the left pointer to the right of the middle index
            l = mid + 1
        # Otherwise
        else:
            # Move the right pointer to the left of the middle index
            r = mid

    # Return the element at the left pointer
    return nums[l]


nums = [1,1,2,3,3,4,4,8,8]
print(singleElement(nums))