#Input: num = 38
#Output: 2
#Explanation: The process is
#38 --> 3 + 8 --> 11
#11 --> 1 + 1 --> 2 
#Since 2 has only one digit, return it.
# Digital root - https://brilliant.org/wiki/digital-root/

def addDigits(num):
    return 0 if num == 0 else (9 if num % 9 == 0 else num % 9)

num = 38
print(addDigits(num))