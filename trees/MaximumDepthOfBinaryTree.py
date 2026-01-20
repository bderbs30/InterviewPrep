# Maximum Depth of Binary Tree
# Easy

# Description
# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest 
# path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: 3

# Example 2:
# Input: root = []
# Output: 0

# Constraints:
# 0 <= The number of nodes in the tree <= 100
# -100 <= Node.val <= 100

# Recommended Time & Space Complexity:
# O(n) time and O(n) space, where n is the number of nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root) -> int:
    """
    Calculate the maximum depth of a binary tree.
    
    Args:
        root: The root node of the binary tree
    
    Returns:
        The maximum depth (number of nodes along the longest path from root to leaf)
    """

    




# Test cases
def test_maxDepth():
    # Note: These tests assume TreeNode class is available
    # Example 1: root = [1,2,3,null,null,4]
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #        \
    #         4
    # Expected depth: 3
    
    # Example 2: root = []
    # Empty tree
    # Expected depth: 0
    
    # Additional test cases would go here
    # Single node tree: depth = 1
    # Linear tree: depth = n
    # Balanced tree: depth = log(n)
    
    print("Test cases would be implemented here")


if __name__ == "__main__":
    test_maxDepth()


# Hints (from NeetCode):
# 
# Hint 1: From the definition of binary tree's maximum depth, Can you think of a way 
#         to achieve this recursively? Maybe you should consider the max depth of the 
#         subtrees first before computing the maxdepth at the root.
#
# Hint 2: We use the Depth First Search (DFS) algorithm to find the maximum depth of 
#         a binary tree, starting from the root. For the subtrees rooted at the left 
#         and right children of the root node, we calculate their maximum depths 
#         recursively going through left and right subtrees. We return 
#         1 + max(leftDepth, rightDepth). Why?
#
# Hint 3: The +1 accounts for the current node, as it contributes to the current depth 
#         in the recursion call. We pass the maximum depth from the current node's left 
#         and right subtrees to its parent because the current maximum depth determines 
#         the longest path from the parent to a leaf node through this subtree.
#
# Solution Approaches:
#
# 1. RECURSIVE DFS (DEPTH-FIRST SEARCH)
#    Intuition: The depth of a tree rooted at a node is 1 (for the current node) plus 
#    the maximum depth of its left and right subtrees. This naturally leads to a recursive 
#    solution where we compute the depth of subtrees first.
#
#    Algorithm:
#    - Base case: If root is None, return 0 (empty tree has depth 0).
#    - Recursive case: Return 1 + max(maxDepth(root.left), maxDepth(root.right)).
#    - The 1 accounts for the current node, and we take the maximum of left and right 
#      subtree depths to find the longest path.
#
#    Time Complexity: O(n) where n is the number of nodes (we visit each node once).
#    Space Complexity: O(h) where h is the height of the tree (recursion stack), 
#                      worst case O(n) for a skewed tree.
#
# 2. ITERATIVE BFS (BREADTH-FIRST SEARCH)
#    Intuition: We can traverse the tree level by level using a queue. The number of 
#    levels we traverse equals the depth of the tree.
#
#    Algorithm:
#    - If root is None, return 0.
#    - Use a queue to store nodes at each level.
#    - Initialize depth = 0 and queue with root.
#    - While queue is not empty:
#      * Increment depth.
#      * Process all nodes at current level (size of queue).
#      * Add children of current level nodes to queue.
#    - Return depth.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(w) where w is the maximum width of the tree (queue size), 
#                      worst case O(n) for a complete binary tree.
#
# 3. ITERATIVE DFS USING STACK
#    Intuition: Use a stack to simulate recursion, storing both the node and its current depth.
#
#    Algorithm:
#    - If root is None, return 0.
#    - Use a stack initialized with (root, 1).
#    - Initialize max_depth = 0.
#    - While stack is not empty:
#      * Pop (node, depth) from stack.
#      * Update max_depth = max(max_depth, depth).
#      * Push (node.left, depth + 1) and (node.right, depth + 1) if they exist.
#    - Return max_depth.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(h) where h is the height of the tree (stack size).
#
# Key Implementation Details:
# - Base case handling: Empty tree (None root) should return 0, not 1.
# - The depth is defined as the number of nodes, not edges. So a single node tree has depth 1.
# - For recursive solution, always check if root is None first to avoid null pointer errors.
# - The recursive approach is typically the most intuitive and concise for this problem.

