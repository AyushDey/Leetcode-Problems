#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#Explanation: Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# res dictionary stores the values as:
# {
#  "aet": ["eat", "tea", "ate"],
#  "ant": ["tan", "nat"],
#  "abt": ["bat"]
# }

from collections import defaultdict
def groupAnagram(strs):
    res = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        res[key].append(s)
    return list(res.values())

#Time Complexity = O(m*n), Space Complexity = O(n*m)
def groupAnagram2(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())


strs = ["eat","tea","tan","ate","nat","bat"]
#print(groupAnagram(strs))
print(groupAnagram(strs))
