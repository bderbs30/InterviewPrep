"""
All Paths From Source to Target

Problem:
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all 
possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from 
node i (i.e., there is a directed edge from node i to graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:
- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., there will be no self-loops)
- All the elements of graph[i] are unique
- The input graph is guaranteed to be a DAG (Directed Acyclic Graph)

Link: https://leetcode.com/problems/all-paths-from-source-to-target/
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # Your code here
        pass
















# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: DFS with Backtracking
    
    Time Complexity: O(2^n * n) - exponential number of paths, each path up to n nodes
    Space Complexity: O(n) - recursion depth and path storage
    
    Key Insight:
    - Use DFS to explore all paths from node 0 to node n-1
    - Since it's a DAG, no cycles - don't need visited set for entire graph
    - But need to track current path to avoid cycles in same path
    - When reaching target (n-1), add current path to result
    - Use backtracking: add node to path, explore, remove node
    '''
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        path = []
        n = len(graph)
        
        def dfs(node):
            # Add current node to path
            path.append(node)
            
            # Base case: reached target
            if node == n - 1:
                result.append(path[:])  # Add copy of path
                path.pop()
                return
            
            # Explore all neighbors
            for neighbor in graph[node]:
                dfs(neighbor)
            
            # Backtrack: remove current node
            path.pop()
        
        dfs(0)
        return result


class Solution2:
    '''
    Approach 2: DFS with Path Passed as Parameter
    
    Time Complexity: O(2^n * n)
    Space Complexity: O(2^n * n) - all paths stored in memory
    
    Key Insight:
    - Pass current path as parameter to each recursive call
    - Creates new list at each level (more memory but cleaner)
    - No need to backtrack/pop since new list created each time
    '''
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []
        n = len(graph)
        
        def dfs(node, path):
            # Add current node to path
            current_path = path + [node]
            
            # Base case: reached target
            if node == n - 1:
                result.append(current_path)
                return
            
            # Explore all neighbors
            for neighbor in graph[node]:
                dfs(neighbor, current_path)
        
        dfs(0, [])
        return result


class Solution3:
    '''
    Approach 3: BFS (Breadth-First Search)
    
    Time Complexity: O(2^n * n)
    Space Complexity: O(2^n * n) - all paths in queue
    
    Key Insight:
    - Use queue to explore paths level by level
    - Each queue element contains a complete path
    - When dequeued node is target, add path to result
    - For all neighbors, create new path and enqueue
    '''
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        from collections import deque
        
        result = []
        n = len(graph)
        queue = deque()
        queue.append([0])  # Start with path containing node 0
        
        while queue:
            path = queue.popleft()
            node = path[-1]  # Last node in path
            
            # If reached target, add to result
            if node == n - 1:
                result.append(path)
                continue
            
            # Explore neighbors
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)
        
        return result


class Solution4:
    '''
    Approach 4: DFS with Memoization (DP)
    
    Time Complexity: O(2^n * n) - still exponential
    Space Complexity: O(2^n * n)
    
    Key Insight:
    - For DAGs, can use memoization to avoid recomputing paths
    - memo[node] = all paths from node to target
    - But since we need ALL paths, memoization doesn't help much
    - This approach still explores all paths
    - More useful for optimization problems (shortest path, etc.)
    '''
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        memo = {}
        n = len(graph)
        
        def dfs(node):
            # If already computed, return
            if node in memo:
                return memo[node]
            
            result = []
            
            # Base case: reached target
            if node == n - 1:
                return [[n - 1]]
            
            # Explore all neighbors
            for neighbor in graph[node]:
                paths_from_neighbor = dfs(neighbor)
                # Prepend current node to all paths from neighbor
                for path in paths_from_neighbor:
                    result.append([node] + path)
            
            memo[node] = result
            return result
        
        return dfs(0)
"""


# Test cases
def test_all_paths_source_target():
    sol = Solution()
    
    # Test case 1
    graph1 = [[1,2],[3],[3],[]]
    result1 = sol.allPathsSourceTarget(graph1)
    print(f"Input: {graph1}")
    print(f"Output: {result1}")
    print(f"Expected: [[0,1,3],[0,2,3]] (order may vary)")
    print()
    
    # Test case 2
    graph2 = [[4,3,1],[3,2,4],[3],[4],[]]
    result2 = sol.allPathsSourceTarget(graph2)
    print(f"Input: {graph2}")
    print(f"Output: {result2}")
    print(f"Expected: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]] (order may vary)")
    print()
    
    # Test case 3: Simple linear path
    graph3 = [[1],[2],[3],[]]
    result3 = sol.allPathsSourceTarget(graph3)
    print(f"Input: {graph3}")
    print(f"Output: {result3}")
    print(f"Expected: [[0,1,2,3]]")
    print()
    
    # Test case 4: Direct path
    graph4 = [[1],[]]
    result4 = sol.allPathsSourceTarget(graph4)
    print(f"Input: {graph4}")
    print(f"Output: {result4}")
    print(f"Expected: [[0,1]]")
    print()


if __name__ == "__main__":
    test_all_paths_source_target()


"""
Key Takeaways:
- Classic graph traversal problem - use DFS or BFS
- Since it's a DAG (no cycles), no need for visited set for entire graph
- Must track current path to avoid cycles within same path
- Use backtracking: add node to path, explore neighbors, remove node
- When reaching target (n-1), add COPY of path to result (path[:])
- Key insight: DAG means nodes can appear in multiple paths, but not twice in same path

Common Mistakes to Avoid:
- Forgetting to make a copy of path when adding to result (using path instead of path[:])
- Not backtracking properly (forgetting to pop after exploring neighbors)
- Using visited set for entire graph (would prevent multiple paths from being found)
- Not handling the case where graph is empty or only has one node
- Confusing DAG property - can visit same node in different paths, just not in same path

Pattern Recognition:
- Graph traversal (DFS/BFS)
- Backtracking for exploring all paths
- Similar to: Word Search, N-Queens (backtracking), but for graphs
- DAG property is key - no cycles means simpler than general graph problems
- Finding all paths vs shortest path (this finds all, not optimal)
"""