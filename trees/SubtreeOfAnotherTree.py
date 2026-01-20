# Subtree of Another Tree
# Easy

# Description
# Given the roots of two binary trees root and subRoot, return true if there is 
# a subtree of root with the same structure and node values of subRoot and false 
# otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and 
# all of this node's descendants. The tree tree could also be considered as a 
# subtree of itself.

# Example 1:
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
# Output: true

# Example 2:
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
# Output: false

# Constraints:
# 1 <= The number of nodes in both trees <= 100
# -100 <= root.val, subRoot.val <= 100

# Recommended Time & Space Complexity:
# O(m * n) time and O(m + n) space, where n and m are the number of nodes in 
# root and subRoot, respectively.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot) -> bool:
    """
    Determine if subRoot is a subtree of root.
    
    Args:
        root: The root node of the main binary tree
        subRoot: The root node of the potential subtree
    
    Returns:
        True if subRoot is a subtree of root, False otherwise
    """




# Helper function to check if two trees are identical
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
def test_isSubtree():
    # Note: These tests assume TreeNode class is available
    # Example 1: root = [1,2,3,4,5], subRoot = [2,4,5]
    # Tree root:           subRoot:
    #       1                  2
    #      / \                / \
    #     2   3              4   5
    #    / \
    #   4   5
    # Expected output: True (subRoot matches subtree rooted at node 2)
    
    # Example 2: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
    # Tree root:           subRoot:
    #       1                  2
    #      / \                / \
    #     2   3              4   5
    #    / \
    #   4   5
    #  /
    # 6
    # Expected output: False (node 4 in root has child 6, but in subRoot it doesn't)
    
    # Additional test cases:
    # - subRoot is the entire root tree: True
    # - subRoot is a single leaf node that exists in root: True
    # - subRoot is empty (None): True (empty tree is subtree of any tree)
    # - root is empty but subRoot is not: False
    
    print("Test cases would be implemented here")


if __name__ == "__main__":
    test_isSubtree()


# Hints (from NeetCode):
# 
# Hint 1: A subtree of a tree is a tree rooted at a specific node. We need to check 
#         whether the given subRoot is identical to any of the subtrees of root. 
#         Can you think of a recursive way to check this? Maybe you can leverage 
#         the idea of solving a problem where two trees are given, and you need to 
#         check whether they are identical in structure and values.
#
# Hint 2: When two trees are identical, it means that every node in both trees has 
#         the same value and structure. We can use the Depth First Search (DFS) 
#         algorithm to solve the problem. How do you implement this?
#
# Hint 3: We traverse the given root, and at each node, we check if the subtree 
#         rooted at that node is identical to the given subRoot. We use a helper 
#         function, sameTree(root1, root2), to determine whether the two trees 
#         passed to it are identical in both structure and values.
#
# Solution Approaches:
#
# 1. RECURSIVE DFS WITH HELPER FUNCTION
#    Intuition: A subtree must match exactly from some node in the main tree. We 
#    need to traverse the main tree and at each node check if the tree rooted at 
#    that node matches subRoot exactly. This requires two separate functions:
#    - isSubtree(): traverses the main tree
#    - isSameTree(): checks if two trees are identical
#
#    Algorithm:
#    - Base case 1: If subRoot is None, return True (empty tree is subtree of any tree).
#    - Base case 2: If root is None but subRoot isn't, return False (can't find subtree).
#    - Check if trees rooted at current node are identical: if isSameTree(root, subRoot), return True.
#    - Recursively check left subtree: isSubtree(root.left, subRoot).
#    - Recursively check right subtree: isSubtree(root.right, subRoot).
#    - Return True if found in either left or right subtree.
#
#    isSameTree helper function:
#    - If both nodes are None, return True.
#    - If one is None, return False.
#    - If values differ, return False.
#    - Recursively check left and right subtrees.
#
#    Time Complexity: O(m * n) where m is the number of nodes in root and n is 
#                     the number of nodes in subRoot. In worst case, we check 
#                     isSameTree at every node in root, and each isSameTree call 
#                     takes O(n) time.
#    Space Complexity: O(m + n) for the recursion stack. The depth of isSubtree 
#                      recursion is O(m) and isSameTree is O(n). In worst case 
#                      (skewed trees), we could have both on the stack.
#
# 2. STRING SERIALIZATION APPROACH
#    Intuition: If we serialize both trees into strings, then checking if subRoot 
#    is a subtree becomes a string matching problem. We can serialize the tree in 
#    preorder traversal and check if subRoot's serialization is a substring of 
#    root's serialization.
#
#    Algorithm:
#    - Serialize both trees using preorder traversal.
#    - Use special markers for null nodes (e.g., "#").
#    - Use delimiters between nodes to avoid false matches (e.g., "1" vs "11").
#    - Check if subRoot's serialization is a substring of root's serialization.
#
#    Time Complexity: O(m + n) for serialization, O(m * n) for string matching 
#                     (or O(m + n) with KMP algorithm).
#    Space Complexity: O(m + n) for storing serialized strings.
#
# 3. HASH-BASED APPROACH
#    Intuition: We can compute a hash value for each subtree and compare hashes 
#    instead of comparing full trees. This can be more efficient in practice but 
#    requires careful hash function design to avoid collisions.
#
#    Algorithm:
#    - Compute hash for subRoot.
#    - Traverse root and compute hash for each subtree.
#    - When hashes match, verify with full comparison (to handle collisions).
#    - A good hash function: hash(node) = node.val + 3 * hash(left) + 7 * hash(right).
#
#    Time Complexity: O(m + n) average case, O(m * n) worst case with collisions.
#    Space Complexity: O(m + n) for recursion and hash storage.
#
# Key Implementation Details:
# - Don't forget the base cases! Especially: empty subRoot is a subtree of any tree.
# - The isSameTree function is crucial and must be implemented correctly.
# - Be careful with the OR logic: isSubtree(root.left, subRoot) OR isSubtree(root.right, subRoot).
# - You must check if current node matches first, before checking children.
# - Common mistake: forgetting that a subtree must include ALL descendants, not just some.
# - The recursive DFS approach with helper function is the most intuitive and recommended.
# - Pattern to remember:
#   * if not subRoot: return True  (empty is subtree of anything)
#   * if not root: return False    (can't find subRoot in empty tree)
#   * if isSameTree(root, subRoot): return True  (found exact match)
#   * return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

