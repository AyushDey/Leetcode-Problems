# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
# Return the number of special letters in word.

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0
# Explanation:
# There are no special characters in word.

# Example 3:
# Input: word = "AbBCab"
# Output: 0
# Explanation:
# There are no special characters in word.

# Constraints:
# 1 <= word.length <= 2 * 105
# word consists of only lowercase and uppercase English letters.


from collections import defaultdict


def numOfSpecialChars2(strs):
    word_hash = defaultdict(int)
    for i, w in enumerate(strs):
        if w.islower():
            word_hash[w] = i
        if w.isupper() and w not in word_hash:
            word_hash[w] = i

    count = 0
    for w, i in word_hash.items():
        if (w.islower() and w.swapcase() in word_hash) and word_hash[w] < word_hash[
            w.swapcase()
        ]:
            count += 1
    return count


def numberOfSpecialChars2Faster(word):
    small = "abcdefghijklmnopqrstuvwxyz"
    capital = "ABCDEFGHIJKLMNOPQRSTUVWQYZ"
    count = 0
    for s, c in zip(small, capital):
        s_idx = word.rfind(s)
        if s_idx < 0:
            continue
        c_idx = word.find(c)
        if c_idx < 0:
            continue
        if s_idx < c_idx:
            count += 1
    return count


if __name__ == "__main__":
    word = "abc"
    word1 = "aaAbcBCA"
    word2 = "cCceDC"
    print(numOfSpecialChars2(word))
    print(numOfSpecialChars2(word1))
    print(numOfSpecialChars2(word2))

    print(numberOfSpecialChars2Faster(word))
    print(numberOfSpecialChars2Faster(word1))
    print(numberOfSpecialChars2Faster(word2))
