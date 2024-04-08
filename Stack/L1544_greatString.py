# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will 
# result "leEeetcode" to be reduced to "leetcode".
"""
    This function takes a string `s` and returns the lexicographically smallest string that can be obtained by removing some characters from `s`.

    Algorithm:
    1. Initialize an empty stack.
    2. Iterate through the characters of the string `s`.
    3. If the stack is not empty and the current character is different from the top of the stack, but their lowercase versions are the same, then pop the top of the stack.
    4. Otherwise, push the current character onto the stack.
    5. After iterating through all characters, join the characters in the stack to form the resulting string.

    Approach:
    This algorithm uses a stack to keep track of the characters that will be included in the resulting string. 
    The key idea is to remove characters that have a corresponding character of the opposite case earlier in the string. 
    This ensures that the resulting string is lexicographically smallest.
"""
def greatString(s):
    stack = []
    i = 0
    while i < len(s):
        if stack and stack[-1] != s[i] and stack[-1].lower() == s[i].lower():
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    return "".join(stack)



s = "leEeetcode"
print(greatString(s))