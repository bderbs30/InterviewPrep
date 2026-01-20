# Diameter of Binary Tree
# Medium

# Description
# The diameter of a binary tree is defined as the length of the longest path between 
# any two nodes within the tree. The path does not necessarily have to pass through 
# the root. The length of a path between two nodes in a binary tree is the number of 
# edges between the nodes. Note that the path cannot include the same node twice.
# 
# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:
# Input: root = [1,null,2,3,4,5]
# Output: 3
# Explanation: The length of the path [1,2,3,5] or [5,3,2,4] is 3.

# Example 2:
# Input: root = [1,2,3]
# Output: 2

# Constraints:
# 1 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100

# Recommended Time & Space Complexity:
# O(n) time and O(n) space, where n is the number of nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root) -> int:
    """
    Calculate the diameter of a binary tree.
    The diameter is the length of the longest path between any two nodes.
    
    Args:
        root: The root node of the binary tree
    
    Returns:
        The diameter (number of edges in the longest path)
    """
    pass


# Test cases
def test_diameterOfBinaryTree():
    # Note: These tests assume TreeNode class is available
    # Example 1: root = [1,null,2,3,4,5]
    # Tree structure:
    #     1
    #      \
    #       2
    #      / \
    #     3   4
    #    /
    #   5
    # Expected diameter: 3 (path [5,3,2,4] or [1,2,3,5])
    
    # Example 2: root = [1,2,3]
    # Tree structure:
    #     1
    #    / \
    #   2   3
    # Expected diameter: 2 (path [2,1,3])
    
    # Additional test cases would go here
    # Single node tree: diameter = 0 (no edges)
    # Linear tree: diameter = n-1 (where n is number of nodes)
    # Balanced tree: diameter could pass through root or be in a subtree
    
    print("Test cases would be implemented here")


if __name__ == "__main__":
    test_diameterOfBinaryTree()


# Hints (from NeetCode):
# 
# Hint 1: The diameter of a binary tree is the longest path between any two nodes. 
#         This path may or may not pass through the root. Can you think of how to 
#         compute this for each node?
#
# Hint 2: For each node, the diameter passing through that node is the sum of the 
#         heights of its left and right subtrees. The overall diameter is the maximum 
#         of all such diameters across all nodes.
#
# Hint 3: Use a depth-first search (DFS) approach. For each node, calculate the height 
#         of its left and right subtrees. The diameter through that node is 
#         leftHeight + rightHeight. Keep track of the maximum diameter found during 
#         the traversal.
#
# Solution Approaches:
#
# 1. RECURSIVE DFS WITH GLOBAL VARIABLE (RECOMMENDED)
#    Intuition: For each node, the diameter passing through that node is the sum of 
#    the heights of its left and right subtrees. We need to find the maximum of all 
#    such diameters. We can use DFS to compute heights and track the maximum diameter 
#    simultaneously.
#
#    Algorithm:
#    - Initialize a global variable max_diameter = 0.
#    - Define a helper function height(node) that:
#      * Returns 0 if node is None.
#      * Recursively computes left_height = height(node.left).
#      * Recursively computes right_height = height(node.right).
#      * Calculates diameter through current node: left_height + right_height.
#      * Updates max_diameter = max(max_diameter, diameter).
#      * Returns 1 + max(left_height, right_height) (height of subtree rooted at node).
#    - Call height(root) to start the traversal.
#    - Return max_diameter.
#
#    Time Complexity: O(n) where n is the number of nodes (we visit each node once).
#    Space Complexity: O(h) where h is the height of the tree (recursion stack), 
#                      worst case O(n) for a skewed tree.
#
# 2. RECURSIVE DFS RETURNING MULTIPLE VALUES
#    Intuition: Instead of using a global variable, we can return both the height and 
#    diameter from each recursive call. This is a more functional programming approach.
#
#    Algorithm:
#    - Define a helper function dfs(node) that returns (height, diameter):
#      * If node is None, return (0, 0).
#      * Recursively get (left_height, left_diameter) = dfs(node.left).
#      * Recursively get (right_height, right_diameter) = dfs(node.right).
#      * Current height = 1 + max(left_height, right_height).
#      * Diameter through current node = left_height + right_height.
#      * Current diameter = max(left_diameter, right_diameter, diameter_through_current).
#      * Return (current_height, current_diameter).
#    - Call dfs(root) and return the diameter from the result.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(h) where h is the height of the tree (recursion stack).
#
# 3. ITERATIVE DFS USING STACK
#    Intuition: Simulate the recursive DFS behavior using an explicit stack. Perform 
#    a post-order traversal and store the height for each visited node in a map.
#
#    Algorithm:
#    - If root is None, return 0.
#    - Use a stack for DFS traversal and a dictionary to store heights.
#    - Initialize max_diameter = 0.
#    - Perform post-order traversal:
#      * Push nodes onto stack with a flag to indicate if we've processed children.
#      * When popping a node, if children are processed:
#        - Get heights of left and right children from dictionary (default 0).
#        - Calculate diameter through current node = left_height + right_height.
#        - Update max_diameter = max(max_diameter, diameter).
#        - Store height of current node = 1 + max(left_height, right_height).
#    - Return max_diameter.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(n) for the stack and height dictionary.
#
# 4. BRUTE FORCE (NOT RECOMMENDED)
#    Intuition: For each node, compute the height of its left and right subtrees. 
#    The diameter through that node is the sum of these heights. Recursively find 
#    the diameter for each node and return the maximum.
#
#    Algorithm:
#    - For each node in the tree:
#      * Calculate height of left subtree.
#      * Calculate height of right subtree.
#      * Diameter through this node = left_height + right_height.
#    - Return the maximum diameter found.
#
#    Time Complexity: O(n²) - for each node, we compute heights which takes O(n).
#    Space Complexity: O(h) for recursion stack.
#
# Key Implementation Details:
# - Important distinction: Diameter is measured in EDGES, not nodes. A path with 
#   3 nodes has 2 edges, so diameter = 2.
# - The diameter path may or may not pass through the root. Always check all nodes.
# - When computing height, return 0 for None nodes (empty subtree has height 0).
# - The diameter through a node = left_height + right_height (sum of heights, not +1).
# - Use a global variable or return multiple values to track the maximum diameter.
# - The recursive DFS approach is typically the most intuitive and efficient.
