#Input  = [2, 5, 9, 11]
#Target = 7
#Output = [0,1]

def two_sum(num, target):
    start, end  = 0, len(num) - 1
    while start < end:
        if num[start] + num[end] == target:
            return [start, end]
        if num[start] + num[end] < target:
            start += 1
        else:
            end -= 1

nums = [2, 5, 9, 11]
target = 7
pos = two_sum(nums, target)
print(pos)
