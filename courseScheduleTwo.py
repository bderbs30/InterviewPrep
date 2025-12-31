# ### Course Schedule II
#
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates
# that you must take course b first if you want to take course a.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first
# take course 1.
#
# There are a total of numCourses courses you are required to take, labeled from
# 0 to numCourses - 1.
#
# Return a valid ordering of courses you can take to finish all courses. If there
# are many valid answers, return any of them. If it's not possible to finish all
# courses, return an empty array.
#
# Example 1:
# Input: numCourses = 3, prerequisites = [[1,0]]
# Output: [0,1,2]
# Explanation: We must ensure that course 0 is taken before course 1.
#
# Example 2:
# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
# Output: []
# Explanation: It's impossible to finish all courses.
#
# Constraints:
# - 1 <= numCourses <= 1000
# - 0 <= prerequisites.length <= 1000
# - All prerequisite pairs are unique.


from typing import List
from collections import defaultdict, deque


def courseScheduleTwo(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # Step 1: Build adjacency list (graph) and in-degree array
    graph = defaultdict(list)  # prereq -> [courses it unlocks]
    in_degree = [0] * numCourses  # How many prerequisites each course has

    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq unlocks course
        in_degree[course] += 1  # course has one more prerequisite

    # Step 2: Initialize queue with courses that have no prerequisites (in-degree = 0)
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    # Step 3: Process courses using BFS (Kahn's Algorithm)
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)

        # "Complete" this course - it unlocks other courses
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1  # One less prerequisite
            if in_degree[neighbor] == 0:  # All prerequisites satisfied!
                queue.append(neighbor)

    # Step 4: Check if all courses were processed
    # If not, there's a cycle (impossible to complete all courses)
    return result if len(result) == numCourses else []


if __name__ == "__main__":
    # Test 1
    numCourses1 = 3
    prerequisites1 = [[1, 0]]
    print(courseScheduleTwo(numCourses1, prerequisites1))  # Expected: [0, 1, 2]

    # Test 2: Cycle exists
    numCourses2 = 3
    prerequisites2 = [[0, 1], [1, 2], [2, 0]]
    print(courseScheduleTwo(numCourses2, prerequisites2))  # Expected: []

    # Test 3: No prerequisites
    numCourses3 = 4
    prerequisites3 = []
    print(
        courseScheduleTwo(numCourses3, prerequisites3)
    )  # Expected: [0, 1, 2, 3] or any order

    # Test 4: Linear dependency
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 1], [3, 2]]
    print(courseScheduleTwo(numCourses4, prerequisites4))  # Expected: [0, 1, 2, 3]
