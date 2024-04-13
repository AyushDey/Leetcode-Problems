# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form 
# the new number 1219 which is the smallest.

# It uses the concept of monotonic increasing order 
# Algo:
# 1. Monotonic increasing order means each element should be greater than the next
# 2. If it isn't we pop the previous element / elements if they are equal or greater
# 3. We only pop till the k limit given

def removeKdigits(num, k):
    stack = []
    # We are checking if the next element is greater than the previous 
    # and if so removing it from the stack otherwise adding it
    for i in num:
        while k > 0 and stack and stack[-1] > i:
            k -= 1
            stack.pop()
        stack.append(i)
    # remove the extra elements from right if not popped
    stack = stack[:len(stack) - k]
    # Storing the result in a variable and converting back to integer 
    # as if there are leading zeros, it will be removed.
    res = ''.join(stack).lstrip('0')
    return res if stack else "0"

num = "10200"
k = 1
print(removeKdigits(num, k))