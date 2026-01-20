# Binary Tree Vertical Order Traversal
# Medium

# Description
# You are given the root node of a binary tree, return the vertical order traversal 
# of its nodes' values.
# For the vertical order traversal, list the nodes column by column starting from 
# the leftmost column and moving to the right.
# Within each column, the nodes should be listed in the order they appear from the 
# top of the tree to the bottom.
# If two nodes are located at the same row and column, the node that appears to 
# the left should come before the other.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Tree structure:
#       3
#      / \
#     9  20
#       /  \
#      15   7
# Column -1: [9]
# Column 0: [3, 15]
# Column 1: [20]
# Column 2: [7]

# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]
# Explanation:
# Tree structure:
#         3
#       /   \
#      9     8
#     / \   / \
#    4   0 1   7
# Column -2: [4]
# Column -1: [9]
# Column 0: [3, 0, 1]
# Column 1: [8]
# Column 2: [7]

# Example 3:
# Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
# Output: [[4],[2,5],[1,10,9,6],[3],[11]]

# Constraints:
# 0 <= number of nodes in the tree <= 100
# -100 <= Node.val <= 100

# Recommended Time & Space Complexity:
# O(n log n) time and O(n) space, where n is the number of nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

def verticalOrder(root):
    """
    Return the vertical order traversal of the binary tree.
    
    Args:
        root: The root node of the binary tree
    
    Returns:
        A list of lists representing nodes grouped by vertical column
    """

    if not root:
        return []


    queue = deque([(root, 0)])
    columns = defaultdict(list)

    result = []

    while queue:
        

        level_size = len(queue)

        for i in range(level_size):
            node, col = queue.popleft()
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

    for col in sorted(columns.keys()):
        result.append(columns[col])

    return result




# Test cases
def test_verticalOrder():
    # Note: These tests assume TreeNode class is available
    
    # Example 1: root = [3,9,20,null,null,15,7]
    # Tree:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    # Expected output: [[9],[3,15],[20],[7]]
    
    # Example 2: root = [3,9,8,4,0,1,7]
    # Tree:
    #         3
    #       /   \
    #      9     8
    #     / \   / \
    #    4   0 1   7
    # Expected output: [[4],[9],[3,0,1],[8],[7]]
    
    # Example 3: Complex tree
    # Expected output: [[4],[2,5],[1,10,9,6],[3],[11]]
    
    # Additional test cases:
    # - Empty tree (None): []
    # - Single node: [[node.val]]
    # - Left-skewed tree: multiple columns going left
    # - Nodes at same row and column: left node comes first
    
    print("Test cases would be implemented here")


if __name__ == "__main__":
    test_verticalOrder()


# Hints:
# 
# Hint 1: Think about how to assign a column number to each node. If the root is 
#         at column 0, what column would its left child be at? What about its 
#         right child?
#
# Hint 2: You need to process nodes level by level (top to bottom) while also 
#         grouping them by column. What traversal method naturally processes 
#         nodes level by level?
#
# Hint 3: Use BFS (level-order traversal) to ensure nodes are processed from top 
#         to bottom. Track each node's column number: left child = parent_column - 1, 
#         right child = parent_column + 1. Group nodes by their column in a dictionary.
#
# Solution Approaches:
#
# 1. BFS WITH COLUMN TRACKING (RECOMMENDED)
#    Intuition: Each node belongs to a vertical column. The root is at column 0, 
#    left children are at column - 1, and right children are at column + 1. We 
#    need to traverse level by level (BFS) to maintain top-to-bottom order within 
#    each column.
#
#    Algorithm:
#    - Use BFS (queue-based) to traverse level by level.
#    - Store tuples of (node, column) in the queue.
#    - Use a dictionary to group nodes by their column: {column: [node_values]}.
#    - Start with root at column 0.
#    - For each node:
#      * Add its value to the list for its column in the dictionary.
#      * Add left child at column - 1 to queue.
#      * Add right child at column + 1 to queue.
#    - After traversal, sort the dictionary by column keys (left to right).
#    - Return the values (lists of nodes) in order.
#
#    Time Complexity: O(n log n) where n is the number of nodes. O(n) for BFS 
#                     traversal, O(n log n) for sorting columns (though typically 
#                     columns are fewer than n).
#    Space Complexity: O(n) for the queue and dictionary.
#
#    Implementation pattern:
#    ```
#    from collections import deque, defaultdict
#    
#    if not root:
#        return []
#    
#    column_table = defaultdict(list)  # {column: [values]}
#    queue = deque([(root, 0)])  # (node, column)
#    
#    while queue:
#        node, col = queue.popleft()
#        
#        # Add node value to its column
#        column_table[col].append(node.val)
#        
#        if node.left:
#            queue.append((node.left, col - 1))
#        if node.right:
#            queue.append((node.right, col + 1))
#    
#    # Sort by column and return values
#    return [column_table[col] for col in sorted(column_table.keys())]
#    ```
#
# 2. BFS WITH MIN/MAX COLUMN TRACKING (OPTIMIZED)
#    Intuition: Instead of using a dictionary and sorting, we can track the minimum 
#    and maximum column numbers encountered. Then iterate through that range to 
#    build the result.
#
#    Algorithm:
#    - Same BFS approach as above.
#    - Track min_column and max_column as we traverse.
#    - Use a dictionary to store nodes by column.
#    - After BFS, iterate from min_column to max_column to build result.
#    - This avoids the sorting step if we track bounds during traversal.
#
#    Time Complexity: O(n) where n is the number of nodes.
#    Space Complexity: O(n) for the queue and dictionary.
#
#    Implementation pattern:
#    ```
#    from collections import deque, defaultdict
#    
#    if not root:
#        return []
#    
#    column_table = defaultdict(list)
#    queue = deque([(root, 0)])
#    min_col = max_col = 0
#    
#    while queue:
#        node, col = queue.popleft()
#        
#        column_table[col].append(node.val)
#        min_col = min(min_col, col)
#        max_col = max(max_col, col)
#        
#        if node.left:
#            queue.append((node.left, col - 1))
#        if node.right:
#            queue.append((node.right, col + 1))
#    
#    # Iterate through column range
#    return [column_table[col] for col in range(min_col, max_col + 1)]
#    ```
#
# 3. DFS WITH LEVEL AND COLUMN TRACKING (INCORRECT APPROACH)
#    Common mistake: Using DFS instead of BFS.
#    
#    Why it fails: DFS doesn't guarantee top-to-bottom order within columns. You 
#    might visit a deeper left node before a shallower right node in the same column.
#    
#    Example where DFS fails:
#    ```
#         1
#        / \
#       2   3
#      /     \
#     4       5
#    ```
#    Column 0 should be [1, 5] (top to bottom)
#    But DFS might give [1, 4] or [5, 1] depending on traversal order.
#
# Key Implementation Details:
# - **Must use BFS, not DFS**: BFS ensures level-by-level processing, which gives 
#   top-to-bottom order within each column automatically.
# - Column calculation:
#   * Root: column 0
#   * Left child: parent_column - 1
#   * Right child: parent_column + 1
# - Use defaultdict(list) for convenient grouping.
# - Don't forget to handle empty tree (return []).
# - Tiebreaker: "If two nodes are at same row and column, left node comes first"
#   → BFS naturally handles this because we process left children before right 
#   children at each node.
#
# Common Mistakes (Where Candidates Go Wrong):
#
# 1. **Using DFS instead of BFS**:
#    - DFS doesn't maintain top-to-bottom order within columns.
#    - You'd need to track levels and sort by level within each column (more complex).
#
# 2. **Forgetting to sort columns**:
#    - Dictionary keys aren't ordered by default (in older Python).
#    - Must sort by column number to get left-to-right order.
#
# 3. **Confusing with other traversal problems**:
#    - This is different from "Vertical Order Traversal" (LC 987) which has 
#      additional sorting requirements within columns.
#    - This problem only requires top-to-bottom order (BFS gives this naturally).
#
# 4. **Not handling negative columns**:
#    - Left children create negative column numbers.
#    - Need to handle full range from min_col to max_col.
#
# 5. **Incorrect column calculation**:
#    - Sometimes candidates use 2*col+1, 2*col+2 (like array heaps).
#    - For vertical order, it's simply col-1 and col+1.
#
# 6. **Overcomplicating the tiebreaker**:
#    - The problem says "left node comes first" for same row and column.
#    - BFS with left-before-right processing handles this automatically.
#    - Don't need extra sorting or complex logic.
#
# Interview Tips:
# - Clarify if empty tree should return [] or None.
# - Ask if column numbers can be negative (yes, they can).
# - Draw out Example 2 to understand column assignments.
# - Mention BFS ensures top-to-bottom order (shows understanding).
# - Optimization: Track min/max columns to avoid sorting (shows advanced thinking).

