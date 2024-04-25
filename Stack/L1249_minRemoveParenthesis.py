#Input: s = "lee(t(c)o)de)"
#Output: "lee(t(c)o)de"
#Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

def minRemove(s):
    stack = []
    s = list(s)
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    for i in stack:
        s[i] = ''
    return ''.join(s)


s = "lee(t(c)o)de)"
print(minRemove(s))