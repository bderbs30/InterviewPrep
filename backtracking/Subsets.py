"""
Subsets

Problem:
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution 
in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [7]
Output: [[],[7]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All numbers in nums are unique

Link: https://neetcode.io/problems/subsets/question?list=neetcode150
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:


        
        
























# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: Backtracking (DFS)
    
    Time Complexity: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
    Space Complexity: O(n) - recursion depth
    
    Key Insight:
    - For each element, we have two choices: include it or exclude it
    - This creates a decision tree with 2^n leaf nodes (subsets)
    - Use backtracking to explore all paths in this decision tree
    - At each index, recursively build subsets with and without current element
    '''
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        
        def backtrack(i):
            # Base case: reached end of array
            if i >= len(nums):
                result.append(subset[:])  # Add copy of current subset
                return
            
            # Decision 1: Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            
            # Decision 2: Exclude nums[i] (backtrack)
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return result


class Solution2:
    '''
    Approach 2: Iterative (Build Up)
    
    Time Complexity: O(n * 2^n)
    Space Complexity: O(1) - excluding output space
    
    Key Insight:
    - Start with empty subset [[]]
    - For each number, add it to all existing subsets to create new subsets
    - Example: [] -> [[], [1]] -> [[], [1], [2], [1,2]] -> ...
    '''
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        
        for num in nums:
            # Add current num to all existing subsets
            result += [curr + [num] for curr in result]
        
        return result


class Solution3:
    '''
    Approach 3: Bit Manipulation
    
    Time Complexity: O(n * 2^n)
    Space Complexity: O(1) - excluding output space
    
    Key Insight:
    - There are 2^n subsets for n elements
    - Each subset can be represented by a binary number
    - If bit i is set, include nums[i] in the subset
    - Example: For [1,2,3], binary 101 represents subset [1,3]
    '''
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        
        # Iterate through all possible binary representations
        for mask in range(1 << n):  # 2^n possibilities
            subset = []
            for i in range(n):
                # Check if i-th bit is set
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        
        return result
"""


# Test cases
def test_subsets():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3]
    result1 = sol.subsets(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]")
    print()
    
    # Test case 2
    nums2 = [7]
    result2 = sol.subsets(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [[],[7]]")
    print()
    
    # Test case 3
    nums3 = [0]
    result3 = sol.subsets(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print()


if __name__ == "__main__":
    test_subsets()


"""
Key Takeaways:
- Backtracking pattern: make decision, recurse, undo decision
- For each element: two choices (include/exclude) -> 2^n subsets
- Always append a COPY of the current subset to result (subset[:])
- Base case: when index reaches end of array
- Three main approaches: backtracking (most intuitive), iterative, bit manipulation

Common Mistakes to Avoid:
- Forgetting to append a copy of subset (using subset[:] or list(subset))
- Not backtracking properly (forgetting to pop/undo the decision)
- Trying to sort or return in specific order (any order is acceptable)
- Confusing this with permutations (order doesn't matter in subsets)

Pattern Recognition:
- Backtracking with decision tree (include/exclude pattern)
- Similar to: Subsets II (with duplicates), Combinations, Permutations
- Key technique: Make decision -> Recurse -> Undo decision
- Time complexity for generating all subsets: O(n * 2^n)
"""
