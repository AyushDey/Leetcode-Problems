# Input : num = 16
# Output : True


def perfectSquare(num):
    if num == 1:
        return True
    l, r = 1, (num//2) + 1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == num:
            return True
        if mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return False



num = int(input())
print(perfectSquare(num))