"""
Populating Next Right Pointers in Each Node

Problem:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
    1
   / \
  2   3
 / \ / \
4  5 6  7

Output: [1,#,2,3,#,4,5,6,7,#]
    1 -> NULL
   / \
  2 -> 3 -> NULL
 / \ / \
4->5->6->7 -> NULL

Explanation: Given the above perfect binary tree, your function should populate each next pointer 
to point to its next right node. The serialized output is in level order with '#' signifying 
the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2^12 - 1]
- -1000 <= Node.val <= 1000

Follow up: 
- You may only use constant extra space.
- The recursive approach is fine. You may assume implicit stack space does not count as extra space.

Link: https://neetcode.io/problems/populating-next-right-pointers-in-each-node
      https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# ============================================================
# YOUR SOLUTION - BFS Approach (Interview Solution)
# ============================================================

from collections import deque

class Solution:
    """
    BFS Level Order Traversal with Queue
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(n) - queue holds up to n/2 nodes at the last level
    """
    def connect(self, root: 'Node') -> 'Node':


        queue = deque([root])
        
        while queue:
            q_len = len(queue)
            
            for cur_idx in range(q_len):
                node = queue.popleft()
                
                if node:
                    if cur_idx < q_len - 1:
                        node.next = queue[0]
                    
                    queue.append(node.left)
                    queue.append(node.right)
        
        return root


# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: Level-by-Level Traversal (Iterative) - Using Previously Established Links
    
    Time Complexity: O(n) - we visit each node exactly once
    Space Complexity: O(1) - only use constant extra space (no queue needed!)
    
    Key Insight:
    - Since it's a PERFECT binary tree, we can use the next pointers we've already established
      on the current level to traverse and connect nodes on the next level
    - For each node, we connect:
      1. left child to right child
      2. right child to next node's left child (if next exists)
    
    Strategy:
    - Start from root (leftmost node of current level)
    - For each level, traverse all nodes using next pointers
    - Connect children of current level nodes
    - Move to next level by going to leftmost.left
    '''
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root as the leftmost node of the first level
        leftmost = root
        
        # Continue until we reach a level with no children (leaf level)
        while leftmost.left:
            # Start with leftmost node of current level
            current = leftmost
            
            # Traverse all nodes at the current level
            while current:
                # Connection 1: Connect left child to right child
                current.left.next = current.right
                
                # Connection 2: Connect right child to next node's left child
                if current.next:
                    current.right.next = current.next.left
                
                # Move to next node in the current level
                current = current.next
            
            # Move to the next level (go to leftmost node of next level)
            leftmost = leftmost.left
        
        return root


class Solution2:
    '''
    Approach 2: Recursive Solution
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(log n) for recursion stack (or O(h) where h is height)
                      O(1) if we don't count recursion stack
    
    Key Insight:
    - Use recursion to establish connections
    - For each node, connect its children and then recurse on left and right subtrees
    '''
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        
        # Connect left child to right child
        root.left.next = root.right
        
        # Connect right child to next node's left child
        if root.next:
            root.right.next = root.next.left
        
        # Recurse on left and right subtrees
        self.connect(root.left)
        self.connect(root.right)
        
        return root


class Solution3:
    '''
    Approach 3: Level Order Traversal with Queue (BFS) - Optimized Version
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(n) - queue can hold up to n/2 nodes at the last level
    
    This approach is more general and works for ANY binary tree (not just perfect trees).
    However, it uses O(n) space which doesn't meet the follow-up requirement.
    '''
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        from collections import deque
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Connect to next node in the same level (except for last node)
                if i < level_size - 1:
                    node.next = queue[0]
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
"""


# Helper function to create a tree from list
def create_tree(values):
    """Creates a tree from a list of values (level order)"""
    if not values:
        return None
    
    root = Node(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def print_tree_with_next_pointers(root):
    """Print tree level by level showing next pointers"""
    if not root:
        print("Empty tree")
        return
    
    leftmost = root
    while leftmost:
        current = leftmost
        level_values = []
        
        while current:
            level_values.append(str(current.val))
            current = current.next
        
        print(" -> ".join(level_values) + " -> NULL")
        leftmost = leftmost.left


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Example tree
    print("Test 1: Perfect binary tree [1,2,3,4,5,6,7]")
    root1 = create_tree([1, 2, 3, 4, 5, 6, 7])
    result1 = solution.connect(root1)
    print_tree_with_next_pointers(result1)
    print()
    
    # Test case 2: Empty tree
    print("Test 2: Empty tree")
    root2 = None
    result2 = solution.connect(root2)
    print_tree_with_next_pointers(result2)
    print()
    
    # Test case 3: Single node
    print("Test 3: Single node [1]")
    root3 = create_tree([1])
    result3 = solution.connect(root3)
    print_tree_with_next_pointers(result3)
    print()
    
    # Test case 4: Larger perfect binary tree
    print("Test 4: Larger tree [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]")
    root4 = create_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    result4 = solution.connect(root4)
    print_tree_with_next_pointers(result4)
    print()


"""
Key Takeaways:
1. Perfect binary tree property allows O(1) space solution
2. Use previously established next pointers to traverse current level
3. Two connections per node: left->right and right->next.left
4. Level-by-level approach avoids using a queue

Common Mistakes to Avoid:
1. Forgetting to check if current.next exists before connecting right child
2. Using a queue (violates O(1) space requirement for perfect tree)
3. Not handling the base case when root is None
4. Confusing this with the general binary tree version (Problem 117)

Pattern Recognition:
- This is a tree traversal + pointer manipulation problem
- Level order processing without explicit queue
- Using "next" pointers to track same-level nodes
"""


"""
=== INTERVIEW SUMMARY ===
Date: January 14, 2026

Pattern: Tree Traversal - Level Order with Pointer Manipulation (BFS pattern, but optimal solution uses previously established pointers)

Key Discussion Points:
- Started with BFS approach using a queue, which is a solid and intuitive solution for level-order traversal problems. Correctly identified that we need to process nodes level-by-level to connect same-level nodes horizontally
- Asked clarifying question about output format: "Are we returning the root node?" This showed awareness that we're modifying in-place. Good instinct to verify expected return value
- Complexity analysis had a critical gap: Initially said space complexity was O(1), but the BFS queue approach actually uses O(n) space since the last level of a perfect binary tree contains roughly n/2 nodes. This is a significant miss given that the follow-up explicitly asks for constant space
- Implementation used level-size tracking with `q_len = len(queue)` and iterated through each level with `for cur_idx in range(q_len)`. This is the standard BFS level-order pattern and works correctly
- Peeking technique: Used `node.next = queue[0]` to set next pointer to the upcoming node in the same level, checking `if cur_idx < q_len - 1` to avoid setting on the last node. Logic works but is slightly verbose (could use if-else instead of two separate ifs)
- Code cleanliness issue: Added children to queue without checking if they exist (`queue.append(node.left)` without `if node.left:`). For leaf nodes, this adds None values to the queue, which then get popped and skipped with `if node:` check. Works but inefficient—wastes iterations on None processing
- Missed the O(1) space optimization entirely: The problem specifically mentions a follow-up about constant space, which is a strong hint that there's a better approach. For perfect binary trees, you can use the next pointers you've already established on the current level to traverse horizontally and connect children on the next level, eliminating the queue entirely
- Did not explore alternative approaches or ask about trade-offs between solutions

Concepts to Review/Practice:
- Understand the difference between O(1) and O(n) space complexity, especially for tree problems where the last level dominates space usage in BFS
- When a problem mentions a follow-up constraint (like "constant space"), that's a signal to think about optimizations beyond the initial approach
- Perfect binary tree property: All levels are fully filled, which enables using established next pointers for horizontal traversal without a queue
- Review the pattern: "Using previously established pointers to avoid auxiliary data structures" - shows up in linked list and tree problems
- Practice identifying when problem constraints (like "perfect binary tree") enable more efficient solutions than general approaches
- Code cleanup: Always check if node.left/node.right exist before appending to avoid processing None values
"""
