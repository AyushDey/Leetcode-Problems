#Input: a = [100,4,200,1,3,2]
#Output: 4

# Time Complexity: O(n), Space Complexity: O(n)
def longestConsecutive(a):
    nums = set(a)
    longest = 0
    for i in a:
        if (i-1) not in nums: # Check if it's the start of a sequence by checki
            length = 0
            while (i+ length) in nums: # Check if the next consecutive element is present
                length+=1
            longest = max(longest,length)
    return longest



a = [100,4,200,1,3,2]
print(longestConsecutive(a))