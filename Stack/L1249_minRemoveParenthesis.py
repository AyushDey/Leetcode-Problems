#Input: s = "lee(t(c)o)de)"
#Output: "lee(t(c)o)de"
#Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

def minRemove(s):
    stack = []
    count = 0
    for i in s:
        if i == '(':
            stack.append(i)
            count += 1
        elif i == ')' and count > 0:
            stack.append(i)
            count -= 1
        elif i != ')':
            stack.append(i)
    
    revst = []
    for i in stack[::-1]:
        if i == '(' and count > 0:
            count -= 1
        else:
            revst.append(i)
    
    return ''.join(revst[::-1])


s = "lee(t(c)o)de)"
print(minRemove(s))