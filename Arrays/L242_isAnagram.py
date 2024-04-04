# Input: s = 'anagram', t = 'nagaram'
# Output: True
# Time Complexity = O(n), Space Complexity = O(n)
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    count= {}
    for i in s:
        count[i] = count.get(i,0) + 1
    for i in t:
        if i in count:
            count[i] -= 1
    for i in count:
        if count[i] != 0:
            return False
    return True
# Time Complexity = O(n), Space Complexity = O(n^2)
def isAnagramMem(s,t):
    if len(s) != len(t):
        return False
    a, b = {}, {}
    for i in range(len(s)):
        a[s[i]] = a.get(s[i], 0) + 1
        b[t[i]] = b.get(t[i], 0) + 1
    for i in a:
        if a[i] != b.get(i, 0):
            return False
    return True
#Time Complexity = O(nlogn), Space Complexity = O(1)
def isAnagramwithoutMemory(s, t):
    return sorted(s) == sorted(t)

s = 'anagram'
t = 'tagaram'
print(isAnagram(s,t))
#print(isAnagramMem(s,t))

