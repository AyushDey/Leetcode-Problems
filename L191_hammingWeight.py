#Input: n = 00000000000000000000000000001011
#Output: 3
#Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

def hamming(n):
    c = 0
    while n:
        n &= (n-1)
        c+=1
    return c

n = 11
print(hamming(n))