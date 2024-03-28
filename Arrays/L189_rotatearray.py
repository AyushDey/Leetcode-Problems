#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums,k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    #print(nums)

nums = list(map(int, input().strip().split()))
k = int(input())
#print(nums)
rotate(nums,k)
print(nums)
