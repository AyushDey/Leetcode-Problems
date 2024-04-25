#Input: s = "()[]{}"
#Output: true

def valid(s):
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{': #Insert opening braces in stack
            stack.append(i)
        if i == ')':
            # not stack means if stack is empty and stack.pop() is 
            # the top value popped
            if not stack or stack.pop() != '(': # Check with the closing brace
                return False
        if i == '}':
            if not stack or stack.pop() != '{': # Check with the closing brace
                return False
        if i == ']':
            if not stack or stack.pop() != '[': # Check with the closing brace
                return False
    # if stack empty return true
    return not stack


s = "[]"
#valid(s)
print(valid(s))