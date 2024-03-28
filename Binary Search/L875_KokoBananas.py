#Input: piles = [3,6,7,11], h = 8
#Output: 4

#Input: piles = [3,6,7,11], h = 8
#Output: 4
#Explanation: Minimum number of bananas Koko can eat to finish all the bananas in the given time (h) 
import math
def koko(piles,h):
    l, r = 1, max(piles) # It forms the range where 
    #l = 1, as Koko has to
    #r = the maximum number of bananas Koko can eat in one go is the set with maximum bananas

    minval = r # As Koko cannot eat anymore than the maximum set
    while l <= r: 
        m = (l+r)//2 # [1,..,mid,..,max]
        totaltime = 0
        for i in piles: # mid * piles[]
            totaltime += math.ceil(i/m) # mid * piles[i] to find time of eat
        if totaltime > h: # [1,..,mid,..,max], mid > h, go left
            l = m + 1
        else: # [1,..,mid,..,max], mid < h, go right
            minval = min(minval, m)
            r = m - 1
    return minval 


piles = list(map(int, input().strip().split()))
h = int(input())
print(koko(piles,h))
