# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}
    val = 0
    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
            val -= roman[s[i]]
        else:
            val += roman[s[i]]
    return val

s = input()
print(romanToInt(s))