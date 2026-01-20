# 74. Search a 2D Matrix
# Medium
# Problem Link: https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150

# Description
# You are given an `m x n` 2-D integer array `matrix` and an integer `target`.
# 
# * Each row in `matrix` is sorted in _non-decreasing_ order.
# * The first integer of every row is greater than the last integer of the previous row.
# 
# Return `true` if `target` exists within `matrix` or `false` otherwise.
# 
# Can you write a solution that runs in `O(log(m * n))` time?

# Example 1:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# Output: true

# Example 2:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
# Output: false

# Constraints:
# * m == matrix.length
# * n == matrix[i].length
# * 1 <= m, n <= 100
# * -10000 <= matrix[i][j], target <= 10000

# Recommended Time & Space Complexity:
# You should aim for a solution with `O(log(m * n))` time and `O(1)` space, where `m` is 
# the number of rows and `n` is the number of columns in the matrix.


from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search for target in a 2D matrix where:
    - Each row is sorted in non-decreasing order
    - The first integer of every row is greater than the last integer of the previous row
    
    Args:
        matrix: An m x n 2D integer array
        target: The integer to search for
    
    Returns:
        True if target exists in matrix, False otherwise
    """
    pass


# Test cases
def test_searchMatrix():
    # Example 1
    matrix1 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    assert searchMatrix(matrix1, 10) == True, "Example 1 failed"
    print("Test 1 passed: Target found in matrix")
    
    # Example 2
    matrix2 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    assert searchMatrix(matrix2, 15) == False, "Example 2 failed"
    print("Test 2 passed: Target not found in matrix")
    
    # Single element matrix - target found
    matrix3 = [[5]]
    assert searchMatrix(matrix3, 5) == True, "Single element found test failed"
    print("Test 3 passed: Single element found")
    
    # Single element matrix - target not found
    matrix4 = [[5]]
    assert searchMatrix(matrix4, 3) == False, "Single element not found test failed"
    print("Test 4 passed: Single element not found")
    
    # Single row matrix
    matrix5 = [[1,3,5,7,9]]
    assert searchMatrix(matrix5, 5) == True, "Single row found test failed"
    assert searchMatrix(matrix5, 6) == False, "Single row not found test failed"
    print("Test 5 passed: Single row matrix")
    
    # Single column matrix
    matrix6 = [[1],[3],[5],[7],[9]]
    assert searchMatrix(matrix6, 5) == True, "Single column found test failed"
    assert searchMatrix(matrix6, 6) == False, "Single column not found test failed"
    print("Test 6 passed: Single column matrix")
    
    # Target at first element
    matrix7 = [[1,3,5],[7,9,11],[13,15,17]]
    assert searchMatrix(matrix7, 1) == True, "First element test failed"
    print("Test 7 passed: Target at first element")
    
    # Target at last element
    matrix8 = [[1,3,5],[7,9,11],[13,15,17]]
    assert searchMatrix(matrix8, 17) == True, "Last element test failed"
    print("Test 8 passed: Target at last element")
    
    # Target smaller than all elements
    matrix9 = [[10,20,30],[40,50,60],[70,80,90]]
    assert searchMatrix(matrix9, 5) == False, "Target too small test failed"
    print("Test 9 passed: Target smaller than all elements")
    
    # Target larger than all elements
    matrix10 = [[10,20,30],[40,50,60],[70,80,90]]
    assert searchMatrix(matrix10, 100) == False, "Target too large test failed"
    print("Test 10 passed: Target larger than all elements")
    
    # Target in middle row
    matrix11 = [[1,2,3],[4,5,6],[7,8,9]]
    assert searchMatrix(matrix11, 5) == True, "Middle row test failed"
    print("Test 11 passed: Target in middle row")
    
    # Negative numbers
    matrix12 = [[-5,-3,-1],[1,3,5],[7,9,11]]
    assert searchMatrix(matrix12, -3) == True, "Negative numbers test failed"
    assert searchMatrix(matrix12, 0) == False, "Negative numbers not found test failed"
    print("Test 12 passed: Negative numbers")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    test_searchMatrix()


# Hints:
# 1. A brute force solution would be to do a linear search on the matrix. This would be 
#    an O(m * n) solution. Can you think of a better way? Maybe an efficient searching 
#    algorithm, as the given matrix is sorted.
# 2. We can use binary search, which is particularly effective when we visualize a row as 
#    a range of numbers, [x, y] where x is the first cell and y is the last cell of a row. 
#    Using this representation, it becomes straightforward to check if the target value 
#    falls within the range.
# 3. We perform a binary search on the rows to identify the row in which the target value 
#    might fall. This operation takes O(log m) time, where m is the number of rows.
# 4. Once we identify the potential row where the target might exist, we can perform a 
#    binary search on that row which acts as a one dimensional array. It takes O(log n) 
#    time, where n is the number of columns in the row.
# 5. Alternatively, you can treat the entire matrix as a single sorted array and perform 
#    one binary search. Convert the 1D index to 2D coordinates: row = index // n, 
#    col = index % n.
# 6. The key insight: the matrix can be treated as a single sorted array because of the 
#    two properties (rows sorted, and first element of row > last element of previous row).

