#Input: num = "35427"
#Output: "35427"
#Explanation: "35427" is already an odd number.

def largestOdd(num):
    stack = []
    maxnum = 0
    for i in num:
        if int(i) & 1:
            stack.append(i)
    
    return stack

num = "3564278"
print(largestOdd(num))