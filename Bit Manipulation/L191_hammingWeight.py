#Input: n = 00000000000000000000000000001011
#Output: 3
#Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''
Why it works:
In binary, subtracting 1 from a number flips all the bits after the rightmost 1 to 0 and the rightmost 1 to 0.
This means that n & (n-1) will be equal to n with the rightmost 1 removed.
Since we’re interested in counting the number of 1s, this operation effectively reduces the count by one each time it’s performed.
'''
def hamming(n):
    '''
    Here we find the number of '1's in the number 
    by decreasing the number in every iteration and 
    performing AND operation everytime with the result:
    In case of 11:
    (11)1011 & (10)1010 = (10)1010
    (10)1010 & (9)1001 = (8)1000
    (8)1000 & (7)0111 = (0)0000 
    '''
    c = 0
    while n:
        n &= (n-1)
        c+=1
    return c

n = 11
print(hamming(n))