# Input: 
# grades = ['a','b','c','e','a']
# n = 3
# k = 2
# Output: a

def gradeImprove(grades, n, k):
    maxgrade = grades[n-1]
    length = len(grades) - 1
    if n == 1:
        for i in range(0,k-1):
            maxgrade = min(maxgrade, grades[i])
    if n-1 == length:
        for i in range(length-1,(length-1) - k,-1):
            #print(grades[i])
            maxgrade = min(maxgrade, grades[i])
    if (n-1)+k > length:
        for i in range(n-1, len(grades)):
            maxgrade = min(maxgrade, grades[i])
        for i in range((n-1)-k, n-1):
            maxgrade = min(maxgrade, grades[i])
    if (n-1) - k < 0:
        for i in range(n, n+k):
            maxgrade = min(maxgrade, grades[i])
        for i in range(0, n):
            maxgrade = min(maxgrade, grades[i])
    if (n-1)+k <= length:
        for i in range(n, n+k):
            maxgrade = min(maxgrade, grades[i])
        for i in range((n-1)-k, n-1):
            maxgrade = min(maxgrade, grades[i])
    
    return maxgrade




grades = list(input().strip().split())
n = int(input())
k = int(input())
#gradeImprove(grades, n, k)
print(gradeImprove(grades, n, k))