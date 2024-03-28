#Input: words = ["cat","bt","hat","tree"], chars = "atach"
#Output: 6
#Explanation: The strings that can be formed are "cat" and "hat" so 
# the answer is 3 + 3 = 6.

def countChar(words, chars):
    for i in words:
        for j in i:
            if j in chars:
                chars.replace(i,"")
    print(chars)


words = ["cat","bt","hat","tree"]
chars = "atach"
countChar(words,chars)
#print(countChar(words,chars))