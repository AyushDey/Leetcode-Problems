#Input: s = "ABAB", k = 2
#Output: 4
#Explanation: Replace the two 'A's with two 'B's or vice versa.


# windowsize - maxcharacter <= k, 
# windowsize represents the current substring, 
# maxcharacter is the most frequent character in window 
# if the replacement is less than k then the window can be increased

#Time complexity: O(26n) (Because it searches the entire hashmap)
#Space complexity: O(n)
from collections import defaultdict
def characterReplacement(s, k):
    res = l = 0
    count = defaultdict(int)

    for r in range(len(s)):
        count[s[r]] += 1
        # max(count.values()) finds the element with highest frequency in the substring
        if (r - l + 1) - max(count.values()) > k: # if the replacement is greater than k then the window can be decreased
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

# Time complexity: O(n)
# Space complexity: O(n)
# Here we fix the maxf to the maximum value as the res increases only if maxf increases
def characterReplacement2(s, k):
    res = l = maxf = 0
    count = defaultdict(int)

    for r in range(len(s)):
        count[s[r]] += 1
        maxf = max(maxf, count[s[r]])
        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


s = "AABABBA"
k = 1
print(characterReplacement(s,k))
print(characterReplacement2(s,k))