#Input: n = 10
#Output: 37
#Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + 
# (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
def totalMoney(n):
    total = 0
    for i in range(n):
        total += i // 7 + i % 7 + 1
    return total

n = 10
output = totalMoney(n)
print(output)