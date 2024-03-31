# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], 
# [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

# Sliding Window approach
# Time complexity: O(n)
# Space complexity: O(1)

def countSubarrays(nums, k):
    max_num = max(nums)
    max_count = l = res = 0
    for r in range(len(nums)):
        #Counting the number of times the maximum element appears in the array
        if nums[r] == max_num: 
            max_count += 1

        # While the max_count is same as k, iteratively shrink the window 
        while max_count == k:
            # When the left pointer is at the maximum element, decrement the max_count so that it can exit 
            # the loop and add the value of l to the result
            if nums[l] == max_num: 
                max_count -= 1
            l += 1
        # Since the left pointer has already moved by 1 place, it suffices the necessity of l + 1 
        # to be added to the result
        res += l

    return res

def countSubarraysVerbose(nums,k):
    # Initialize variables to track the maximum element, its count, and the sliding window boundaries
    max_num = max(nums)
    max_count = l = res = 0

    # Iterate through the array using a sliding window approach
    for r in range(len(nums)):
        # If the current element is the maximum element, increment its count
        if nums[r] == max_num:
            max_count += 1

        # While the maximum element count exceeds k or
        # if max_count is exactly same and the value of the left boundary is not equal to the maximum element 
        # both signifies that the window can be shrunk further
        while max_count > k or (l <= r and max_count == k and nums[l] != max_num):
            # If the element at the left boundary is the maximum element, decrement its count
            if nums[l] == max_num:
                max_count -= 1
            l += 1

        # If the maximum element count is equal to k, add the length of the current window to the result
        if max_count == k:
            res += l + 1
        
    return res


nums = [1,3,2,3,3]
k = 2
print(countSubarraysVerbose(nums,k))
print(countSubarrays(nums,k))