#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by 
# array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.

# Algo
# Step 1 : Set left and right pointer
# Step 2 : Set leftmax and rightmax
# Step 3 : Create a while loop l < r, where:
# Step 3a: if lmax < rmax, increase l, set lmax to max(lmax, height[l]), 
# add res += lmax - height[l]
# Step 3b: else, decrease r, set rmax to max(rmax, height[r]), 
# add res += rmax - height[r]
# Step 4: return res 

def trap(height):
    if not height: return 0

    l, r = 0, len(height) - 1 # Left and right pointers to keep track of current value
    lmax, rmax = height[l], height[r] # Left Max height, Right max height
    res = 0
    while l < r:
        if lmax < rmax: 
            l += 1
            lmax = max(lmax, height[l])
            res += lmax - height[l]
        else:
            r -= 1
            rmax = max(rmax, height[r])
            res += rmax - height[r]
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))