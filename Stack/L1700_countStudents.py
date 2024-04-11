#Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
#Output: 0 
#Explanation:
#- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
#- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
#- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
#- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
#- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
#- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
#- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
#- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
#Hence all students are able to eat.

from collections import Counter
def countStudents(students, sandwiches):
    res = len(students)
    count = Counter(students)

    for s in sandwiches:
        if count[s] > 0:
            res -= 1
            count[s] -= 1
        else:
            return res
    return res


students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(countStudents(students,sandwiches))
