# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of 
# the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". 
# This compresses to "a2b2c3".


def stringCompression(chars):
    count = 1
    j = 0
    if len(chars) == 1:
        return 1
    for i in range(1, len(chars) + 1):
        if i < len(chars) and chars[i] == chars[i-1]:
            count += 1
        else:
            chars[j] = chars[i-1]
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
            count = 1
    return j
    
    

chars = ["a","a","b","b","c","c","c"]
print(stringCompression(chars))
print(chars)