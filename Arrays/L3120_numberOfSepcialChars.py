# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3

# Explanation:
# The special characters in word are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0

# Explanation:
# No character in word appears in uppercase.

def countSpecial(word):
    count = set(word)
    return sum(s.swapcase() in count for s in count if s.islower())

if __name__ == '__main__':
    word = "aaAbcBC"
    word1 = "abBCab"
    print(countSpecial(word))
    print(countSpecial(word1))