#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#Explanation: Given n pairs of parentheses, 
# write a function to generate all combinations of well-formed parentheses.

def parenthesis(n):
    stack = []
    res = []

    def backtracking(opeN, closeD):
        if opeN == closeD == n: # when Open braces = Closed braces = Max number of each (n). 
            res.append(''.join(stack)) # Adds the combination to the result matrix
            return
        if opeN < n: # Number of Open braces < Max number. 
            stack.append('(') # Add an open brace
            backtracking(opeN+1, closeD) # Increase the count of open braces
            stack.pop() 
        if closeD < opeN: # When Closed braces < Open braces.
            stack.append(')') # More Close braces to be added
            backtracking(opeN, closeD+1) # Increase the count of close braces
            stack.pop()

    backtracking(0,0) # base case
    return res


n = 3
print(parenthesis(n))