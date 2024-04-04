#Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
#Output: 3
#Explanation:
#The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
#The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
#The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
#Note that no other cars meet these fleets before the destination, so the answer is 3.

# Stack used
def carFleet(target, position, speed):
    pair = [[p,s] for p, s in zip(position, speed)]
    pair.sort(reverse=True) # Sorting it because we want to go in reverse order
    stack = []
    #for p, s in sorted(pair.items(), reverse=True):
    # Since we are travelling the opposite direction, we need to reverse the pair
    for p, s in pair:
        t = (target - p)/s # Time taken for a car to reach the distance at its speed
        stack.append(t) # Add the time to the top of the stack
        if len(stack) > 1 and stack[-1] <= stack[-2]: # If the time taken is less than the time taken by the previous car
            stack.pop() # We assume it as one single fleet and remove the top of the stack which consists the time taken by the previous car
    return len(stack)

#No extra memory other than the pair
def carFleet1(target, position, speed):
    cars = list(zip(position, speed))
    cars.sort(reverse=True)
    fleet = last = 0
    for p, s in cars:
        time = (target - p) / s
        if time > last:
            fleet += 1
            last = time
    return fleet

target = 12 
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))
print(carFleet1(target, position, speed))