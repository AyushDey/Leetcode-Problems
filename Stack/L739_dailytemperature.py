# Input: [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def temp(a):
    stack = []
    n = len(a)
    res = [0]*n
    for i in range(n):
        t = a[i]
        while stack and a[stack[-1]] < t:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res


#a = list(map(int, input().split()))
a = [73,74,75,71,69,72,76,73]
print(temp(a))