#Input: s = "egg", t = "add"
#Output: true

def isIsomporphic(s,t):
    STmap, TSmap = {}, {}
    for c1, c2 in zip(s,t):
        if (c1 in STmap and STmap[c1] != c2) or (c2 in TSmap and TSmap[c2] != c1):
            return False
        STmap[c1] = c2
        TSmap[c2] = c1 
    return True

s = "egg"
t = "add"
print(isIsomporphic(s,t))