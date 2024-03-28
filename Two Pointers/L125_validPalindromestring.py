# A valid palindrome is a string that reads the same forwards and backwards, 
# ignoring non-alphanumeric characters and case sensitivity.
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

def valpal(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l+=1
            r-=1
    return True


s = 'A man, a plan, a canal: Panama'
print(valpal(s))