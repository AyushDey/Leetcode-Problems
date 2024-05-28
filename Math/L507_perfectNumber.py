# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.

def perfectNum(num):
    if num == 1:
        return False
    sum = 1
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            sum += i + num//i
    return num == sum

num = int(input())
print(perfectNum(num))