# Binary Search
# Easy

# Description
# You are given an array of distinct integers nums, sorted in ascending order, 
# and an integer target.

# Implement a function to search for target within nums. If it exists, then return 
# its index, otherwise, return -1.

# Your solution must run in O(log n) time.

# Example 1:
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

# Example 2:
# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1

# Constraints:
# 1 <= nums.length <= 10000
# -10000 < nums[i], target < 10000
# All the integers in nums are unique.

# Recommended Time & Space Complexity:
# O(log n) time and O(1) space, where n is the size of the input array.

#     if low > high:
#         return -1


def binary_search(low, high, nums, target):

    if low > high:
        return -1

    middle_idx = low + (high - low) // 2

    if target == nums[middle_idx]:
        return middle_idx

    if nums[middle_idx] > target:
        return binary_search(low, middle_idx - 1, nums, target)

    elif nums[middle_idx] < target:
        return binary_search(middle_idx + 1, high, nums, target)

    return -1




# def binary_search(l: int, r: int, nums, target: int) -> int:
#         if l > r:
#             return -1
#         m = l + (r - l) // 2

#         if nums[m] == target:
#             return m
#         if nums[m] < target:
#             return binary_search(m + 1, r, nums, target)
#         return binary_search(l, m - 1, nums, target)


def search(nums: list[int], target: int) -> int:
    """
    Search for target in a sorted array of distinct integers using binary search.
    
    Args:
        nums: A sorted array of distinct integers in ascending order
        target: The integer to search for
    
    Returns:
        The index of target if it exists, otherwise -1.
    """
    # binary search has a low mid high - so for each search we need to determine
    # its also recursive so we need to have the nested function call within the function

    # if mid is greater than or less than value 

    # if mid is greater than value search over low - mid

    # if mid is less than value search over mid - high

    # [-1,0,2,4,6,8]
    #   0 1 2 3 4 

    answer = binary_search(0, len(nums) - 1, nums, target)

    print(answer)

    return answer





# Test cases
def test_search():
    # Example 1
    assert search([-1,0,2,4,6,8], 4) == 3, "Example 1 failed"
    
    # Example 2
    assert search([-1,0,2,4,6,8], 3) == -1, "Example 2 failed"
    
    # Additional test cases
    
    # Single element - target found
    assert search([5], 5) == 0, "Single element found test failed"
    
    # Single element - target not found
    assert search([5], 3) == -1, "Single element not found test failed"
    
    # Two elements - target found
    assert search([1, 3], 1) == 0, "Two elements - first test failed"
    assert search([1, 3], 3) == 1, "Two elements - second test failed"
    
    # Two elements - target not found
    assert search([1, 3], 2) == -1, "Two elements - not found test failed"
    
    # Target at beginning
    assert search([1, 2, 3, 4, 5], 1) == 0, "Target at beginning test failed"
    
    # Target at end
    assert search([1, 2, 3, 4, 5], 5) == 4, "Target at end test failed"
    
    # Target in middle
    assert search([1, 2, 3, 4, 5], 3) == 2, "Target in middle test failed"
    
    # Negative numbers
    assert search([-5, -3, -1, 0, 2, 4], -3) == 1, "Negative numbers test failed"
    assert search([-5, -3, -1, 0, 2, 4], -4) == -1, "Negative numbers not found test failed"
    
    # Large array
    assert search(list(range(100)), 50) == 50, "Large array test failed"
    assert search(list(range(100)), 100) == -1, "Large array not found test failed"
    
    # Target smaller than all elements
    assert search([1, 2, 3, 4, 5], 0) == -1, "Target smaller than all test failed"
    
    # Target larger than all elements
    assert search([1, 2, 3, 4, 5], 6) == -1, "Target larger than all test failed"
    
    # Odd length array
    assert search([1, 3, 5, 7, 9], 5) == 2, "Odd length array test failed"
    
    # Even length array
    assert search([1, 3, 5, 7], 5) == 2, "Even length array test failed"
    
    # Array with gaps
    assert search([1, 5, 10, 15, 20], 10) == 2, "Array with gaps test failed"
    assert search([1, 5, 10, 15, 20], 12) == -1, "Array with gaps not found test failed"
    
    # Edge case: minimum constraint values
    assert search([-9999, 0, 9999], 0) == 1, "Edge case minimum values test failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_search()


# Hints (from NeetCode):
# 
# Basic Hints:
# 1. Can you find an algorithm that is useful when the array is sorted? Maybe other than linear search.
# 2. The problem name is the name of the algorithm that we can use. We need to find a target value and if 
#    it does not exist in the array return -1. We have l and r as the boundaries of the segment of the 
#    array in which we are searching. Try building conditions to eliminate half of the search segment 
#    at each step. Maybe sorted nature of the array can be helpful.
# 3. We compare the target value with the mid of the segment. For example, consider the array [1, 2, 3, 4, 5] 
#    and target = 4. The mid value is 3, thus, on the next iteration we search to the right of mid. 
#    The remaining segment is [4,5]. Why?
# 4. Because the array is sorted, all elements to the left of mid (including 3) are guaranteed to be smaller 
#    than the target. Therefore, we can safely eliminate that half of the array from consideration, narrowing 
#    the search to the right half and repeat this search until we find the target.
#
# Solution Approaches (from NeetCode):
#
# 1. RECURSIVE BINARY SEARCH
#    Intuition: Binary search works by repeatedly cutting the search space in half. Instead of scanning the 
#    entire array, we check the middle element:
#    - If it's the target → return the index.
#    - If the target is larger → search only in the right half.
#    - If the target is smaller → search only in the left half.
#    The recursive version simply expresses this idea as a function that keeps calling itself on the appropriate 
#    half until the target is found or the range becomes invalid.
#
#    Algorithm:
#    - Define a recursive function that takes the current search range [l, r].
#    - If l > r, the range is empty → return -1.
#    - Compute the middle index m = (l + r) // 2 (or l + (r - l) // 2 to avoid overflow).
#    - Compare nums[m] with target:
#      * If equal → return m.
#      * If nums[m] < target → recursively search [m + 1, r].
#      * If nums[m] > target → recursively search [l, m - 1].
#    - Start the recursion with the full range [0, n - 1].
#
#    Time Complexity: O(log n)
#    Space Complexity: O(log n) due to recursion stack
#
# 2. ITERATIVE BINARY SEARCH (RECOMMENDED)
#    Intuition: Binary search checks the middle element of a sorted array and decides which half to discard.
#    Instead of using recursion, the iterative approach keeps shrinking the search range using a loop.
#    We adjust the left and right pointers until we either find the target or the pointers cross, meaning 
#    the target isn't present.
#
#    Algorithm:
#    - Initialize two pointers: l = 0 (start of array), r = len(nums) - 1 (end of array).
#    - While l <= r:
#      * Compute m = l + (r - l) // 2 (safe midpoint to avoid overflow).
#      * If nums[m] == target, return m.
#      * If nums[m] < target, move search to the right half: update l = m + 1.
#      * If nums[m] > target, move search to the left half: update r = m - 1.
#    - If the loop ends without finding the target, return -1.
#
#    Time Complexity: O(log n)
#    Space Complexity: O(1)
#
# 3. UPPER BOUND APPROACH
#    Intuition: Upper bound binary search finds the first index where a value greater than the target appears.
#    Once we know that position, the actual target—if it exists—must be right before it. So instead of 
#    directly searching for the target, we search for the boundary where values stop being ≤ target. Then 
#    we simply check whether the element just before that boundary is the target.
#
#    Algorithm:
#    - Set l = 0 and r = len(nums) (right is one past the last index).
#    - While l < r:
#      * Compute midpoint m.
#      * If nums[m] > target, shrink the right side → r = m.
#      * Otherwise (nums[m] <= target), shrink the left side → l = m + 1.
#    - After the loop: l is the upper bound (first index where nums[l] > target).
#    - So the potential location of the target is l - 1.
#    - If l > 0 and nums[l - 1] == target, return l - 1.
#    - Otherwise, return -1 (target not found).
#
#    Time Complexity: O(log n)
#    Space Complexity: O(1)
#
# 4. LOWER BOUND APPROACH
#    Intuition: Lower bound binary search finds the first index where a value is greater than or equal to 
#    the target. This means if the target exists in the array, this lower-bound index will point exactly 
#    to its first occurrence. So instead of directly searching for equality, we search for the leftmost 
#    position where the target could appear, then verify it.
#
#    Algorithm:
#    - Initialize: l = 0, r = len(nums) (right is one past the last index).
#    - While l < r:
#      * Compute midpoint m.
#      * If nums[m] >= target, shrink the search to the left half → r = m.
#      * Otherwise (nums[m] < target), search in the right half → l = m + 1.
#    - After the loop: l is the lower bound (first index where value ≥ target).
#    - If l is within bounds and nums[l] == target, return l.
#    - Otherwise, return -1 (the target is not in the array).
#
#    Time Complexity: O(log n)
#    Space Complexity: O(1)
#
# 5. BUILT-IN FUNCTION (Python)
#    Python's bisect module provides bisect_left which implements lower bound binary search.
#    - Use bisect.bisect_left(nums, target) to find the lower bound.
#    - Check if the returned index is valid and contains the target.
#    - Return the index if found, otherwise -1.
#
#    Example: import bisect
#             index = bisect.bisect_left(nums, target)
#             return index if index < len(nums) and nums[index] == target else -1
#
#    Time Complexity: O(log n)
#    Space Complexity: O(1)
#
# Key Implementation Details:
# - Use l + (r - l) // 2 instead of (l + r) // 2 to avoid integer overflow in other languages.
# - The loop condition l <= r (for iterative) ensures you check all possible positions.
# - The array is guaranteed to have distinct integers, so you don't need to handle duplicates.
# - Since the array is sorted in ascending order, you can use this property to determine which half to search.
# - The key insight: because the array is sorted, you can eliminate half of the remaining elements at each step.

