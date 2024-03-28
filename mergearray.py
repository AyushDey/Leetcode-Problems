# Two arrays given num1 and num2. Merge them and remove any 0s or ' '
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: nums1 = [1,2,2,3,5,6]

def merge(nums1, nums2, m, n):
    for i in range(m, m+n):
        nums1[i] = nums2[i-m]
    nums1.sort()
    

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, nums2, m=3, n = 3)
print(nums1)