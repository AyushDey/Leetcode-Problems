'''
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
'''
from collections import Counter
def mostEven(nums):
    val = [(x,y) for x,y in Counter(nums).items() if x % 2 == 0]    
    maxval = 0
    mineven = -1
    for k, v in val:
        if v > maxval:
            maxval = v
            mineven = k
        if v == maxval:
            mineven = min(mineven, k)
    return mineven
        
nums = list(map(int, input().strip().split()))
#[8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
print(mostEven(nums))