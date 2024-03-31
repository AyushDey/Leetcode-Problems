# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Sliding window
# Time complexity: O(n)
# Space complexity: O(n)

# Using dictionary
from collections import defaultdict
def longestSubstringWithoutRepeat(s):
    count = defaultdict(int)
    l = res = 0
    for r in range(len(s)):
        count[s[r]] += 1
        while count[s[r]] > 1:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

# Using set
def longestSubstringWithoutRepeatSet(s):
    count = set()
    l = res = 0
    for r, c in enumerate(s):
        while c in count:
            count.remove(s[l])
            l += 1
        count.add(c)
        res = max(res, r - l + 1)
    return res

s = "pwwkew"
print(longestSubstringWithoutRepeat(s))
print(longestSubstringWithoutRepeatSet(s))