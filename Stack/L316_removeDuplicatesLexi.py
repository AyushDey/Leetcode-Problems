# Input: s = "cbacdcbc"
# Output: "acdb"


def removeDuplicate(s):
    res = []
    for i in range(len(s)):
        if s[i] not in res:
            j = len(res) - 1
            while j >= 0 and res[j] > s[i] and res[j] in s[i+1:]:
                res.pop()
                j -= 1
            res.append(s[i])
    return ''.join(res)


s = "cbacdcbc"
print(removeDuplicate(s))