#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

def courseSchedule(numCourses, prerequisites):
    # Adjacency list where {course: prerequisites}
    adjlist = {i:[] for i in range(numCourses)}
    for c, pre in prerequisites:
        adjlist[c].append(pre)
    
    visited = set()
    def dfs(c):
        if c in visited: # Current course previously visited, hence a loop
            return False
        if adjlist[c] == []:
            return True
        visited.add(c)
        for p in adjlist[c]:
            if not dfs(p) : return False
        visited.remove(c)
        adjlist[c] = []
        return True
    for c in range(numCourses):
        if not dfs(c): return False
    return True


numCourses = 2
prerequisites = [[1,0]]
print(courseSchedule(numCourses, prerequisites))
