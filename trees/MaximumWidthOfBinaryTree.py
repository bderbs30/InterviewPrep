# Maximum Width of Binary Tree
# Medium

# Description
# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the 
# leftmost and rightmost non-null nodes), where the null nodes between the 
# end-nodes that would be present in a complete binary tree extending down to 
# that level are also counted into the length calculation.
# It is guaranteed that the answer will be in the range of a 32-bit signed integer.

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
# Tree structure:
#          1
#        /   \
#       3     2
#      / \     \
#     5   3     9
# Level 0: 1 node, width = 1
# Level 1: 2 nodes (3,2), width = 2
# Level 2: 4 positions (5,3,null,9), width = 4

# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 
# (6,null,null,null,null,null,7).

# Example 3:
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).

# Constraints:
# The number of nodes in the tree is in the range [1, 3000]
# -100 <= Node.val <= 100

# Recommended Time & Space Complexity:
# O(n) time and O(w) space, where n is the number of nodes and w is the 
# maximum width of the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root) -> int:
    """
    Calculate the maximum width of a binary tree.
    
    Args:
        root: The root node of the binary tree
    
    Returns:
        The maximum width among all levels of the tree
    """




# Test cases
def test_widthOfBinaryTree():
    # Note: These tests assume TreeNode class is available
    # Example 1: root = [1,3,2,5,3,null,9]
    # Tree structure:
    #          1
    #        /   \
    #       3     2
    #      / \     \
    #     5   3     9
    # Expected output: 4
    
    # Example 2: root = [1,3,2,5,null,null,9,6,null,7]
    # Expected output: 7
    
    # Example 3: root = [1,3,2,5]
    # Tree structure:
    #       1
    #      / \
    #     3   2
    #    /
    #   5
    # Expected output: 2
    
    # Additional test cases:
    # - Single node tree: width = 1
    # - Complete binary tree: width = number of nodes at last level
    # - Skewed tree (all left or all right): width = 1
    
    print("Test cases would be implemented here")


if __name__ == "__main__":
    test_widthOfBinaryTree()


# Hints:
# 
# Hint 1: Can you think of a way to assign a position/index to each node as if 
#         the tree were a complete binary tree? In a complete binary tree stored 
#         as an array, if a node is at index i, its left child is at 2*i and 
#         right child is at 2*i + 1.
#
# Hint 2: If you use BFS (level-order traversal) and track each node's position, 
#         how can you calculate the width of each level? The width would be the 
#         difference between the rightmost and leftmost positions, plus 1.
#
# Hint 3: To avoid integer overflow with very deep trees, consider normalizing 
#         the positions at each level by subtracting the position of the leftmost 
#         node. This keeps the numbers manageable while preserving relative distances.
#
# Solution Approaches:
#
# 1. BFS WITH POSITION TRACKING (RECOMMENDED)
#    Intuition: Treat the binary tree as if it were stored in an array (like a heap).
#    Each node gets a position index: if parent is at position p, left child is 
#    at 2*p and right child is at 2*p + 1. The width of a level is the distance 
#    between the leftmost and rightmost nodes at that level.
#
#    Algorithm:
#    - Use BFS (queue-based) to traverse level by level.
#    - Store tuples of (node, position) in the queue.
#    - Start with root at position 0 (or 1).
#    - For each level:
#      * Track the leftmost position (first node in level).
#      * Track the rightmost position (last node in level).
#      * Calculate width = rightmost - leftmost + 1.
#      * Update max_width if current width is larger.
#    - When adding children to queue:
#      * Left child position = 2 * parent_position
#      * Right child position = 2 * parent_position + 1
#    - To prevent overflow, normalize positions at each level by subtracting 
#      the leftmost position.
#
#    Time Complexity: O(n) where n is the number of nodes (visit each node once).
#    Space Complexity: O(w) where w is the maximum width (queue size at widest level).
#
#    Implementation pattern:
#    ```
#    from collections import deque
#    
#    max_width = 0
#    queue = deque([(root, 0)])  # (node, position)
#    
#    while queue:
#        level_size = len(queue)
#        level_start = queue[0][1]  # Position of leftmost node
#        
#        for i in range(level_size):
#            node, pos = queue.popleft()
#            
#            if node.left:
#                queue.append((node.left, 2 * pos))
#            if node.right:
#                queue.append((node.right, 2 * pos + 1))
#        
#        # Width = position of rightmost - position of leftmost + 1
#        width = pos - level_start + 1
#        max_width = max(max_width, width)
#    
#    return max_width
#    ```
#
# 2. DFS WITH POSITION TRACKING
#    Intuition: Use DFS to traverse the tree while tracking both the level (depth) 
#    and position of each node. Store the leftmost position seen at each level, 
#    and calculate width by comparing current position with leftmost at same level.
#
#    Algorithm:
#    - Use a dictionary to store the leftmost position at each level.
#    - Traverse tree using DFS (can be preorder).
#    - For each node at (level, position):
#      * If this is the first node at this level, store its position.
#      * Calculate width = current_position - leftmost_position[level] + 1.
#      * Update max_width if current width is larger.
#    - Recurse on children with:
#      * Left child: (level + 1, 2 * position)
#      * Right child: (level + 1, 2 * position + 1)
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(h) for recursion stack, where h is height.
#
#    Implementation pattern:
#    ```
#    def widthOfBinaryTree(root):
#        leftmost = {}  # level -> leftmost position at that level
#        max_width = [0]  # Use list to modify in nested function
#        
#        def dfs(node, level, pos):
#            if not node:
#                return
#            
#            # Record leftmost position at this level
#            if level not in leftmost:
#                leftmost[level] = pos
#            
#            # Calculate width at this level
#            width = pos - leftmost[level] + 1
#            max_width[0] = max(max_width[0], width)
#            
#            # Recurse on children
#            dfs(node.left, level + 1, 2 * pos)
#            dfs(node.right, level + 1, 2 * pos + 1)
#        
#        dfs(root, 0, 0)
#        return max_width[0]
#    ```
#
# Key Implementation Details:
# - Position indexing: Start from 0 or 1 (both work, but be consistent).
# - The formula for children positions is crucial:
#   * Left child = 2 * parent_pos (if starting from 0, add offset if needed)
#   * Right child = 2 * parent_pos + 1
# - Overflow prevention: For very deep trees, positions can get huge. 
#   Normalize by subtracting leftmost position at each level.
# - Width calculation: rightmost_pos - leftmost_pos + 1 (the +1 is important!)
# - This problem is different from just counting nodes at each level - null nodes 
#   in the middle count toward the width!
# - BFS approach is generally more intuitive for this problem since we naturally 
#   process level by level.
# - Common mistakes:
#   * Forgetting to add 1 in width calculation
#   * Not handling overflow for deep trees
#   * Confusing this with "count nodes at each level" problem

