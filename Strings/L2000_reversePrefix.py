# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

def reversePrefix(word, ch):
    if ch not in word:
        return word
    n = word.index(ch)
    word = word[n::-1] + word[n+1:]
    return word

word = "abcdefd"
ch = 'd'
print(reversePrefix(word, ch))