#Input: s = "(1+(2*3)+((8)/4))+1"
#Output: 3
#Explanation: Digit 8 is inside of 3 nested parentheses in the string.


def maxDepth(s):
    res = 0
    op = 0
    for i in s:
        res = max(res,op)
        if i == '(':
            op += 1
        elif i == ')':
            op -= 1
    return res



s = "(1)+(((2))+(((3)))"
print(maxDepth(s))