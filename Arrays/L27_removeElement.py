#Input: nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3,_,_,_]
#Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
#Note that the five elements can be returned in any order.
#It does not matter what you leave beyond the returned k (hence they are underscores).

def removeElement(nums,val):
    index = 0 
    for i in range(len(nums)): 
        if nums[i] != val: #Checks if the number is equal to the val
            nums[index] = nums[i] # If not the puts the value of the current in the index
            index += 1 # increases index
        # If the value is same then the index stays the same
    return index

nums = list(map(int, input().strip().split()))
val = 2
#removeElement(nums,val)
print(removeElement(nums,val))