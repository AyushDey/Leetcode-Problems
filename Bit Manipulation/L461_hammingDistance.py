'''
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''
def hammingDistance(x,y):
    a = x ^ y
    c = 0
    while a:
        a &= (a-1)
        c += 1
    return c

def hammingDistanceMincode(x,y):
    return bin(x ^ y).count('1')

x = int(input())
y = int(input())
print(hammingDistance(x,y))
#print(hammingDistanceMincode(x,y))