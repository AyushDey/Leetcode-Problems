#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by 
# array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.

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