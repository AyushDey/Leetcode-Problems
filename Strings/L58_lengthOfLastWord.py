#Input: s = "Hello World"
#Output: 5
#Explanation: The last word is "World" with length 5.

def lengthOfLastWord(s):
    slen = s.split()
    return len(slen[-1])
def lengthOfLastWord1(s):
    p, lenword = len(s) - 1, 0
    while s[p] == ' ':
        p -= 1
    while p >= 0 and s[p] != ' ':
        lenword += 1
        p -= 1
    return lenword

s = "Hello  World  "
print(lengthOfLastWord(s))
print(lengthOfLastWord1(s))