#Input: tokens = ["4","13","5","/","+"]
#Output: 6
#Explanation: (4 + (13 / 5)) = 6

def ReversePolish(arr):
    stack = []
    for i in arr:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        elif i == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif i == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    return stack[0]

arr = ["4","13","5","/","+"]
print(ReversePolish(arr))