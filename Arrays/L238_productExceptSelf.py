#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]

def productExceptSelf(nums):
    output = [1] * len(nums) # List to store the result
    # Pass 1 to traverse and add the prefix values
    pre = 1
    for i in range(len(nums)):
        output[i] = pre 
        pre *= nums[i] # [1, 1, 2, 6]
    # Pass 2 to traverse and multiply prefix values with postfix
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i]*= post
        post*= nums[i]

    return output

nums = [1,2,3,4]
#productExceptSelf(nums)
print(productExceptSelf(nums))

