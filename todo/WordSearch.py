# 79. Word Search
# Medium

# Description
# Given an m x n grid of characters board and a string word, return true if word 
# exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where 
# adjacent cells are horizontally or vertically neighboring. The same letter cell 
# may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?


def exist(board: list[list[str]], word: str) -> bool:
    """
    Determine if a word exists in the board by moving to adjacent cells.
    
    Args:
        board: An m x n grid of characters
        word: The word to search for
    
    Returns:
        True if the word exists in the board, False otherwise.
    """
    pass


# Test cases
def test_exist():
    # Example 1
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCCED") == True, "Example 1 failed"
    
    # Example 2
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "SEE") == True, "Example 2 failed"
    
    # Example 3
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCB") == False, "Example 3 failed"
    
    # Additional test cases
    
    # Single character word
    board = [["A"]]
    assert exist(board, "A") == True, "Single character word test failed"
    assert exist(board, "B") == False, "Single character not found test failed"
    
    # Single row board
    board = [["A","B","C"]]
    assert exist(board, "ABC") == True, "Single row test failed"
    assert exist(board, "CBA") == False, "Single row reverse test failed"
    
    # Single column board
    board = [["A"],["B"],["C"]]
    assert exist(board, "ABC") == True, "Single column test failed"
    
    # Word that requires backtracking
    board = [["A","B"],["C","D"]]
    assert exist(board, "ABDC") == False, "Backtracking test failed (can't reuse cells)"
    
    # Word with repeated characters
    board = [["A","A"],["A","A"]]
    assert exist(board, "AAAA") == True, "Repeated characters test failed"
    
    # Word that doesn't exist
    board = [["A","B"],["C","D"]]
    assert exist(board, "ACBD") == True, "Diagonal-like path test failed"
    assert exist(board, "ABCD") == False, "Invalid path test failed"
    
    # Larger board
    board = [["A","B","C","D"],["E","F","G","H"],["I","J","K","L"]]
    assert exist(board, "ABCDHLKJIFE") == True, "Larger board test failed"
    
    # Word longer than any possible path
    board = [["A","B"],["C","D"]]
    assert exist(board, "ABCDE") == False, "Word too long test failed"
    
    # Case sensitivity (if applicable - constraints say both cases)
    board = [["a","B"],["C","d"]]
    assert exist(board, "aB") == True, "Mixed case test failed"
    
    # Empty word (edge case - though constraints say length >= 1)
    # This test is for robustness
    board = [["A"]]
    # Note: According to constraints, word.length >= 1, so we skip empty word test
    
    # Word that requires going back and forth (should fail)
    board = [["A","B","C"],["D","E","F"],["G","H","I"]]
    assert exist(board, "ABED") == False, "Back and forth path test failed"
    
    # Simple 2x2 case
    board = [["a","b"],["c","d"]]
    assert exist(board, "ac") == True, "Simple 2x2 vertical test failed"
    assert exist(board, "ab") == True, "Simple 2x2 horizontal test failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_exist()


# Hints:
# 1. This is a classic backtracking problem - use DFS (Depth-First Search).
# 2. Start from each cell in the board and try to find the word starting from that cell.
# 3. For each cell, check if it matches the first character of the word.
# 4. Use a visited set or mark cells as visited to avoid using the same cell twice in a path.
# 5. Explore all four directions: up, down, left, right (horizontally and vertically).
# 6. When exploring a cell, mark it as visited, recursively search for the next character, then unmark it (backtrack).
# 7. Base case: if you've matched all characters in the word, return True.
# 8. Pruning: if the current cell doesn't match the current character, return False immediately.
# 9. Make sure to check bounds before accessing board cells (row and column indices).
# 10. You can modify the board temporarily (mark as visited with a special character) or use a separate visited matrix.
# 11. If modifying the board, remember to restore it after backtracking (change it back to original character).
# 12. Consider early termination: if you find the word, return True immediately without exploring further.
# 13. The word can start from any cell in the board, so iterate through all cells as starting points.
# 14. Use a helper function that takes current position (row, col) and current index in the word.
# 15. For optimization: check if remaining characters in word can fit in remaining unvisited cells.
# 16. Since the board is small (m, n <= 6), you don't need to worry too much about optimization, but pruning helps.
# 17. Remember: adjacent means only horizontally or vertically, NOT diagonally.
# 18. The same letter cell cannot be used more than once in the same path, but can be used in different paths.

