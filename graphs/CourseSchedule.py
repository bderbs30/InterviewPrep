"""
Course Schedule

Problem:
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you 
must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to 
numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:
Input: numCourses = 2, prerequisites = [[0,1]]
Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you 
must take course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 1000
- 0 <= prerequisites.length <= 1000
- prerequisites[i].length == 2
- 0 <= a[i], b[i] < numCourses
- All prerequisite pairs are unique.

Link: https://neetcode.io/problems/course-schedule/question
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Your code here
        pass


# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: DFS with Cycle Detection
    
    Time Complexity: O(V + E) where V = numCourses, E = prerequisites.length
    Space Complexity: O(V + E) for adjacency list and recursion stack
    
    Key Insight:
    - Model as directed graph: course -> prerequisite (edge from a to b)
    - Problem reduces to detecting cycles in directed graph
    - If cycle exists, impossible to complete all courses
    - Use DFS with two states: visiting (in current path) and visited (fully processed)
    - If we encounter a node that's currently "visiting", we found a cycle
    - Three states: unvisited (0), visiting (1), visited (2)
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # State: 0 = unvisited, 1 = visiting (in current path), 2 = visited (fully processed)
        state = [0] * numCourses
        
        def hasCycle(course):
            # If currently visiting, we found a cycle
            if state[course] == 1:
                return True
            
            # If already visited, no cycle from this node
            if state[course] == 2:
                return False
            
            # Mark as visiting
            state[course] = 1
            
            # Check all prerequisites
            for prereq in graph[course]:
                if hasCycle(prereq):
                    return True
            
            # Mark as visited (fully processed)
            state[course] = 2
            return False
        
        # Check all courses for cycles
        for course in range(numCourses):
            if state[course] == 0:  # Only check unvisited
                if hasCycle(course):
                    return False
        
        return True


class Solution2:
    '''
    Approach 2: DFS with Path Set
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    
    Key Insight:
    - Similar to Solution1 but uses a set to track current path
    - More intuitive: if node in current path, cycle detected
    - Clear path set when backtracking
    - Use visited set to avoid revisiting fully processed nodes
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = set()  # Fully processed nodes
        path = set()     # Nodes in current DFS path
        
        def hasCycle(course):
            # If in current path, cycle detected
            if course in path:
                return True
            
            # If already fully processed, no cycle
            if course in visited:
                return False
            
            # Add to current path
            path.add(course)
            
            # Check all prerequisites
            for prereq in graph[course]:
                if hasCycle(prereq):
                    return True
            
            # Remove from path (backtrack) and mark as visited
            path.remove(course)
            visited.add(course)
            return False
        
        # Check all courses
        for course in range(numCourses):
            if course not in visited:
                if hasCycle(course):
                    return False
        
        return True


class Solution3:
    '''
    Approach 3: Kahn's Algorithm (Topological Sort with BFS)
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    
    Key Insight:
    - If graph has no cycles, we can perform topological sort
    - Count in-degrees for each node
    - Start with nodes having in-degree 0 (no prerequisites)
    - Process nodes, reduce in-degrees of neighbors
    - If we can process all nodes, no cycle exists
    - If some nodes remain unprocessed, cycle exists
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        from collections import deque
        
        # Build adjacency list and in-degree count
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Reverse: prereq -> course
            in_degree[course] += 1
        
        # Start with courses having no prerequisites
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        processed = 0
        
        # Process courses
        while queue:
            course = queue.popleft()
            processed += 1
            
            # Reduce in-degree of dependent courses
            for dependent in graph[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        # If all courses processed, no cycle
        return processed == numCourses


class Solution4:
    '''
    Approach 4: DFS with Memoization (Optimized)
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    
    Key Insight:
    - Similar to Solution1 but with memoization
    - Once we determine a node has no cycle, cache result
    - Avoids redundant DFS calls
    - More efficient for graphs with many paths to same nodes
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # memo[course] = True if no cycle from this course, False if cycle exists
        memo = {}
        path = set()
        
        def hasCycle(course):
            # If in current path, cycle detected
            if course in path:
                return True
            
            # If already computed, return cached result
            if course in memo:
                return memo[course]
            
            # Add to current path
            path.add(course)
            
            # Check all prerequisites
            for prereq in graph[course]:
                if hasCycle(prereq):
                    memo[course] = True
                    path.remove(course)
                    return True
            
            # No cycle found, remove from path and cache result
            path.remove(course)
            memo[course] = False
            return False
        
        # Check all courses
        for course in range(numCourses):
            if course not in memo:
                if hasCycle(course):
                    return False
        
        return True
"""


# Test cases
def test_course_schedule():
    sol = Solution()
    
    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[0, 1]]
    result1 = sol.canFinish(numCourses1, prerequisites1)
    print(f"Input: numCourses = {numCourses1}, prerequisites = {prerequisites1}")
    print(f"Output: {result1}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[0, 1], [1, 0]]
    result2 = sol.canFinish(numCourses2, prerequisites2)
    print(f"Input: numCourses = {numCourses2}, prerequisites = {prerequisites2}")
    print(f"Output: {result2}")
    print(f"Expected: False")
    print()
    
    # Test case 3: No prerequisites
    numCourses3 = 3
    prerequisites3 = []
    result3 = sol.canFinish(numCourses3, prerequisites3)
    print(f"Input: numCourses = {numCourses3}, prerequisites = {prerequisites3}")
    print(f"Output: {result3}")
    print(f"Expected: True")
    print()
    
    # Test case 4: Complex valid schedule
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result4 = sol.canFinish(numCourses4, prerequisites4)
    print(f"Input: numCourses = {numCourses4}, prerequisites = {prerequisites4}")
    print(f"Output: {result4}")
    print(f"Expected: True")
    print()
    
    # Test case 5: Single course
    numCourses5 = 1
    prerequisites5 = []
    result5 = sol.canFinish(numCourses5, prerequisites5)
    print(f"Input: numCourses = {numCourses5}, prerequisites = {prerequisites5}")
    print(f"Output: {result5}")
    print(f"Expected: True")
    print()


if __name__ == "__main__":
    test_course_schedule()


"""
Key Takeaways:
- This is a cycle detection problem in a directed graph
- Model prerequisites as edges: course -> prerequisite (directed edge)
- If cycle exists, impossible to complete all courses
- Three main approaches: DFS with state tracking, DFS with path set, or Kahn's algorithm (BFS)
- DFS approach uses three states: unvisited, visiting (in current path), visited (fully processed)
- Key insight: if we encounter a node that's "visiting" during DFS, we found a cycle
- Kahn's algorithm: count in-degrees, process nodes with in-degree 0, if all processed = no cycle
- Time complexity: O(V + E) for all approaches
- Space complexity: O(V + E) for adjacency list and auxiliary data structures

Common Mistakes to Avoid:
- Building graph incorrectly: remember prerequisites[i] = [a, b] means b is prerequisite for a
- Not handling disconnected components: need to check all courses, not just one
- Forgetting to mark nodes as "visited" after processing: leads to infinite loops
- Confusing "visiting" vs "visited": visiting = in current path (cycle check), visited = fully processed
- Not clearing path set when backtracking in DFS approach
- In Kahn's algorithm: forgetting to process all nodes or not checking if processed count equals numCourses
- Edge case: empty prerequisites should return True (all courses can be taken)

Pattern Recognition:
- Graph cycle detection in directed graphs
- Topological sort (Kahn's algorithm variant)
- DFS with state tracking (three-color algorithm)
- Similar to: Course Schedule II, Alien Dictionary, Build Order
- Core pattern: detecting cycles in dependency graphs
- This is a fundamental graph problem that appears in many variations
"""
