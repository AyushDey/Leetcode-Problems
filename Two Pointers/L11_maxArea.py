# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented 
# by array [1,8,6,2,5,4,8,3,7]. In this case, the 
# max area of water (blue section) the container can contain is 49.

def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    while l != r:
        area = min(height[l], height[r]) * (r-l)
        res = max(res, area)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1

    return res



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
