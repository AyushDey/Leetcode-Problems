# Input: [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
'''
def temp(a):
    k = []
    for i in range(len(a)):
        l = 0
        for j in range(i, len(a)):
            l+=1
            if a[i] < a[j]:
                l+=1
            else:
                k.append(i)
    print(k)
'''
def temp(a):
    stack = []
    n = len(a)
    res = [0]*n
    for i in range(len(a)):
        t = a[i]
        while stack != [] and a[stack[-1]] < t:
            index = stack.pop()
            res[index] = i - index
        stack.append(i)
    return res


a = list(map(int, input().split()))
print(temp(a))