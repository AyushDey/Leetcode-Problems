#Input: sequence = "ababc", word = "ab"
#Output: 2
#Explanation: "abab" is a substring in "ababc".


def maxString(sequence, word):
    wordlen = len(word)
    sequencelen = len(sequence)
    c = 0
    for i in range(1, ((sequencelen // wordlen)+ 1)):
        if word*i in sequence: # in python3 word * i = wordwordword
            c = i

    return c

sequence = input()
word  = input()
print(maxString(sequence,word))