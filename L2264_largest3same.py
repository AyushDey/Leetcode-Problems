#Input: num = "6777133339"
#Output: "777"
#Explanation: There are two distinct good integers: "777" and "333".
#"777" is the largest, so we return "777".

def largestGood(num):
    maxval = -1
    for i in range(len(num) - 2):
        if num[i] == num[i+1] == num[i+2]:
           maxval = max(maxval, int(num[i]))
    return "" if maxval == -1 else  str(maxval)*3

num = input()
print(largestGood(num))