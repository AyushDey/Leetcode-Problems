#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums,k):
    # Calculate the actual number of steps to rotate by taking the modulus of k with the length of the list.
    k = k % len(nums)
    # Slice the list into two parts: nums[last k elements] and nums[0 to k elements]
    # Concatenate the two parts of the list
    nums[:] = nums[-k:] + nums[:-k]
    
nums = list(map(int, input().strip().split()))
k = int(input())
#print(nums)
rotate(nums,k)
print(nums)
