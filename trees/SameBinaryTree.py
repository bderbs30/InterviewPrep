# Same Binary Tree
# Easy

# Description
# Given the roots of two binary trees p and q, return true if the trees are 
# equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same 
# structure and the nodes have the same values.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [4,7], q = [4,null,7]
# Output: false

# Example 3:
# Input: p = [1,2,3], q = [1,3,2]
# Output: false

# Constraints:
# 0 <= The number of nodes in both trees <= 100
# -100 <= Node.val <= 100

# Recommended Time & Space Complexity:
# O(n) time and O(n) space, where n is the number of nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q) -> bool:
    """
    Determine if two binary trees are structurally identical and have the same node values.
    
    Args:
        p: The root node of the first binary tree
        q: The root node of the second binary tree
    
    Returns:
        True if the trees are identical, False otherwise
    """

    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)






# Test cases
def test_isSameTree():
    # Note: These tests assume TreeNode class is available
    # Example 1: p = [1,2,3], q = [1,2,3]
    # Tree p:           Tree q:
    #     1                 1
    #    / \               / \
    #   2   3             2   3
    # Expected output: True
    
    # Example 2: p = [4,7], q = [4,null,7]
    # Tree p:           Tree q:
    #     4                 4
    #    /                   \
    #   7                     7
    # Expected output: False
    
    # Example 3: p = [1,2,3], q = [1,3,2]
    # Tree p:           Tree q:
    #     1                 1
    #    / \               / \
    #   2   3             3   2
    # Expected output: False
    
    # Additional test cases:
    # - Both trees are empty (None): True
    # - One tree is empty, other is not: False
    # - Single node trees with same value: True
    # - Single node trees with different values: False
    
    print("Test cases would be implemented here")


if __name__ == "__main__":
    test_isSameTree()


# Hints (from NeetCode):
# 
# Hint 1: Can you think of an algorithm that is used to traverse the tree? 
#         Maybe in terms of recursion.
#
# Hint 2: We can use the Depth First Search (DFS) algorithm to traverse the tree. 
#         Can you think of a way to simultaneously traverse both the trees?
#
# Hint 3: We traverse both trees starting from their root nodes. At each step in 
#         the recursion, we check if the current nodes in both trees are either 
#         null or have the same value. If one node is null while the other is not, 
#         or if their values differ, we return false. If the values match, we 
#         recursively check their left and right subtrees. If any recursive call 
#         returns false, the result for the current recursive call is false.
#
# Solution Approaches:
#
# 1. RECURSIVE DFS (DEPTH-FIRST SEARCH)
#    Intuition: Two trees are the same if their roots have the same value and 
#    their left and right subtrees are also the same. This naturally leads to 
#    a recursive solution where we compare nodes at each level.
#
#    Algorithm:
#    - Base case 1: If both p and q are None, return True (both empty trees are the same).
#    - Base case 2: If one is None and the other isn't, return False (different structure).
#    - Base case 3: If p.val != q.val, return False (different values).
#    - Recursive case: Return isSameTree(p.left, q.left) AND isSameTree(p.right, q.right).
#    - Both left and right subtrees must be the same for the trees to be identical.
#
#    Time Complexity: O(n) where n is the number of nodes in the smaller tree 
#                     (we visit each node once until we find a difference or 
#                     reach the end).
#    Space Complexity: O(h) where h is the height of the tree (recursion stack), 
#                      worst case O(n) for a skewed tree.
#
# 2. ITERATIVE BFS (BREADTH-FIRST SEARCH)
#    Intuition: We can use a queue to traverse both trees level by level simultaneously,
#    comparing corresponding nodes at each step.
#
#    Algorithm:
#    - If both p and q are None, return True.
#    - If one is None and the other isn't, return False.
#    - Use a queue (or deque) to store pairs of corresponding nodes from both trees.
#    - Initialize queue with (p, q).
#    - While queue is not empty:
#      * Dequeue a pair of nodes (node1, node2).
#      * If both are None, continue.
#      * If one is None or their values differ, return False.
#      * Enqueue their corresponding left children: (node1.left, node2.left).
#      * Enqueue their corresponding right children: (node1.right, node2.right).
#    - If we complete the traversal without finding differences, return True.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(w) where w is the maximum width of the tree (queue size), 
#                      worst case O(n) for a complete binary tree.
#
# 3. ITERATIVE DFS USING STACK
#    Intuition: Use a stack to simulate recursion, storing pairs of corresponding 
#    nodes from both trees.
#
#    Algorithm:
#    - Similar to BFS approach but using a stack instead of a queue.
#    - Initialize stack with (p, q).
#    - While stack is not empty:
#      * Pop a pair of nodes (node1, node2).
#      * If both are None, continue.
#      * If one is None or their values differ, return False.
#      * Push (node1.left, node2.left) and (node1.right, node2.right).
#    - Return True if we complete the traversal.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(h) where h is the height of the tree (stack size).
#
# Key Implementation Details:
# - Order matters: Check if both nodes are None first before checking if one is None.
# - Must check both left and right subtrees - both must match for trees to be identical.
# - The base cases are crucial: handle None values carefully to avoid null pointer errors.
# - For recursive solution, the most common pattern is:
#   * if not p and not q: return True
#   * if not p or not q: return False  (one is None, other isn't)
#   * if p.val != q.val: return False
#   * return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
# - The recursive approach is typically the most intuitive and concise for this problem.

