# 797. All Paths From Source to Target
# Medium

# Description
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all 
# possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from 
# node i (i.e., there is a directed edge from node i to node graph[i][j]).

# Example 1:
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Example 2:
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

# Constraints:
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.


def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    """
    Find all possible paths from node 0 to node n-1 in a directed acyclic graph.
    
    Args:
        graph: A list where graph[i] contains all nodes reachable from node i
    
    Returns:
        A list of all paths from node 0 to node n-1, where each path is a list of nodes.
    """
    pass


# Test cases
def test_allPathsSourceTarget():
    # Example 1
    result = allPathsSourceTarget([[1,2],[3],[3],[]])
    expected = [[0,1,3],[0,2,3]]
    assert sorted(result) == sorted(expected), f"Example 1 failed: expected {expected}, got {result}"
    
    # Example 2
    result = allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
    expected = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    assert sorted(result) == sorted(expected), f"Example 2 failed: expected {expected}, got {result}"
    
    # Additional test cases
    
    # Simple linear path
    result = allPathsSourceTarget([[1],[2],[3],[]])
    expected = [[0,1,2,3]]
    assert sorted(result) == sorted(expected), "Linear path test failed"
    
    # Direct path from 0 to target
    result = allPathsSourceTarget([[1],[]])
    expected = [[0,1]]
    assert sorted(result) == sorted(expected), "Direct path test failed"
    
    # Single path with multiple options
    result = allPathsSourceTarget([[1,2],[3],[3],[]])
    expected = [[0,1,3],[0,2,3]]
    assert sorted(result) == sorted(expected), "Multiple paths test failed"
    
    # Graph with branching and merging
    result = allPathsSourceTarget([[1,2],[3],[3],[4],[]])
    expected = [[0,1,3,4],[0,2,3,4]]
    assert sorted(result) == sorted(expected), "Branching and merging test failed"
    
    # Multiple paths with different lengths
    result = allPathsSourceTarget([[1,2],[3],[1,3],[4],[]])
    expected = [[0,1,3,4],[0,2,1,3,4],[0,2,3,4]]
    assert sorted(result) == sorted(expected), "Multiple path lengths test failed"
    
    # Graph where 0 has no direct connection to target
    result = allPathsSourceTarget([[1],[2],[3],[]])
    expected = [[0,1,2,3]]
    assert sorted(result) == sorted(expected), "No direct connection test failed"
    
    # Complex graph with many paths
    result = allPathsSourceTarget([[1,2,3],[4],[4],[4],[5],[]])
    expected = [[0,1,4,5],[0,2,4,5],[0,3,4,5]]
    assert sorted(result) == sorted(expected), "Complex graph test failed"
    
    # Graph with multiple paths to same intermediate node
    result = allPathsSourceTarget([[1,2],[3],[3],[4,5],[6],[6],[]])
    expected = [[0,1,3,4,6],[0,1,3,5,6],[0,2,3,4,6],[0,2,3,5,6]]
    assert sorted(result) == sorted(expected), "Multiple intermediate paths test failed"
    
    # Smallest possible graph
    result = allPathsSourceTarget([[1],[]])
    expected = [[0,1]]
    assert sorted(result) == sorted(expected), "Smallest graph test failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_allPathsSourceTarget()


# Hints:
# 1. This is a classic graph traversal problem - use DFS (Depth-First Search) or BFS (Breadth-First Search).
# 2. Since it's a DAG (no cycles), you don't need to worry about visiting the same node twice in a path.
# 3. Start from node 0 and explore all possible paths until you reach node n-1.
# 4. Use backtracking: add current node to path, explore neighbors, then remove node when backtracking.
# 5. When you reach the target node (n-1), add the current path to your result list.
# 6. You can use recursion with a current path list that you build as you traverse.
# 7. Make sure to make a copy of the path when adding it to results, not a reference.
# 8. The graph representation: graph[i] gives you all neighbors of node i.
# 9. Since the graph is small (n <= 15), you don't need to worry about optimization too much.
# 10. You can use a helper function that takes the current node and current path as parameters.
# 11. For each neighbor of the current node, recursively explore paths from that neighbor.
# 12. Base case: if current node == n-1, you've found a complete path.
# 13. You can also use iterative DFS with a stack if you prefer iterative over recursive approach.
# 14. Remember: since it's a DAG, you can visit nodes multiple times in different paths, but not in the same path.
# 15. Consider using list.copy() or list[:] to create a copy of the path before adding to results.

