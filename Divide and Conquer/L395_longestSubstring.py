#Input: s = "aaabb", k = 3
#Output: 3
#Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
from collections import defaultdict
def longestSubstring(s, k): 
    if not s or len(s) < k: # Checks if the string is empty or if the length of the string is less than k
        return 0
    for c in set(s): # Checks if the character is present in the string
        if s.count(c) < k: # Checks if the character is present less than k times
            return max(longestSubstring(substring, k) for substring in s.split(c)) # Recursively calls the function for each substring

    return len(s) 


s = "aaabb"
k = 3
print(longestSubstring(s, k))
