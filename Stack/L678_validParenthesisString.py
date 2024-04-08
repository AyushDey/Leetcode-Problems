# Input: s = "(*))"
# Output: true

def validParenthesisString(s):
    # lmin is the lowest possible open parenthesis 
    # lmax is the highest possible open parenthesis
    # lmin should never turn 0 as lmin and lmax are the valid range of possibilities
    lmin = lmax = 0
    for c in s:
        if c == '(':
            lmin += 1
            lmax += 1
        elif c == ')':
            lmin = max(0, lmin - 1) 
            lmax -= 1
        else:
            lmin = max(0, lmin - 1)
            lmax += 1
        # if lmax is -ve which means it encountered closing braces 
        # before opening and hence can never be valid
        if lmax < 0:
            return False
    return lmin == 0


s = "(*))"
print(validParenthesisString(s))