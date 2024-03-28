#Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
#Output: 3
def carFleet(target, position, speed):
    pair = [[p,s] for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    #for p, s in sorted(pair.items(), reverse=True):
    for p, s in pair:
        stack.append((target - p)/s)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


target = 12 
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))