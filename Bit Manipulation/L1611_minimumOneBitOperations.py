#Input: n = 3
#Output: 2
#Explanation: The binary representation of 3 is "11".
#"11" -> "01" with the 2nd operation since the 0th bit is 1.
#"01" -> "00" with the 1st operation.

def minOneBit(n):
    s = bin(n)
    for i in s:
        print(i)

n = 10
print(minOneBit(n))