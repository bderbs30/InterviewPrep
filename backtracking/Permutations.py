"""
Permutations

Problem:
Given an array nums of unique integers, return all the possible permutations. 
You may return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [7]
Output: [[7]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All integers in nums are unique

Link: https://neetcode.io/problems/permutations/question?list=neetcode150
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Your code here
        pass
































# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: Backtracking with Boolean Array
    
    Time Complexity: O(n * n!) - n! permutations, each takes O(n) to copy
    Space Complexity: O(n) - recursion depth + boolean array
    
    Key Insight:
    - Unlike combinations/subsets, ORDER MATTERS in permutations
    - Each permutation uses every element exactly once
    - Use a boolean array to track which elements are already used
    - At each step, try adding any unused element
    '''
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        used = [False] * len(nums)
        
        def backtrack(curr):
            # Base case: permutation is complete
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            
            # Try each number that hasn't been used yet
            for i in range(len(nums)):
                if not used[i]:
                    # Choose
                    curr.append(nums[i])
                    used[i] = True
                    
                    # Explore
                    backtrack(curr)
                    
                    # Unchoose (backtrack)
                    curr.pop()
                    used[i] = False
        
        backtrack([])
        return result


class Solution2:
    '''
    Approach 2: Backtracking with Set
    
    Time Complexity: O(n * n!)
    Space Complexity: O(n)
    
    Key Insight:
    - Instead of boolean array, use a set to track used elements
    - Check if element is in set (O(1) lookup)
    - Add/remove from set during backtracking
    '''
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(curr, used):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            
            for num in nums:
                if num not in used:
                    curr.append(num)
                    backtrack(curr, used | {num})  # Create new set with num
                    curr.pop()
        
        backtrack([], set())
        return result


class Solution3:
    '''
    Approach 3: Swap-based Backtracking (In-place)
    
    Time Complexity: O(n * n!)
    Space Complexity: O(n) - only recursion stack
    
    Key Insight:
    - Swap elements to generate permutations in-place
    - At each position, try swapping with every element from current position onwards
    - No need for extra boolean array or set
    - More space efficient but modifies input (can copy first)
    '''
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(start):
            # Base case: reached end
            if start == len(nums):
                result.append(nums[:])
                return
            
            # Try swapping current position with each element from start onwards
            for i in range(start, len(nums)):
                # Swap
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recurse
                backtrack(start + 1)
                
                # Swap back (backtrack)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result


class Solution4:
    '''
    Approach 4: Backtracking by Building from Remaining
    
    Time Complexity: O(n * n!)
    Space Complexity: O(n^2) - creating new lists at each level
    
    Key Insight:
    - Pass remaining available numbers as parameter
    - At each step, try each remaining number
    - Create new list without chosen number for next recursion
    - Less efficient (more memory) but conceptually simple
    '''
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(curr, remaining):
            if not remaining:
                result.append(curr[:])
                return
            
            for i in range(len(remaining)):
                # Choose remaining[i]
                backtrack(curr + [remaining[i]], 
                         remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return result
"""


# Test cases
def test_permutations():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3]
    result1 = sol.permute(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] (order may vary)")
    print(f"Count: {len(result1)} (expected 6)")
    print()
    
    # Test case 2
    nums2 = [7]
    result2 = sol.permute(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [[7]]")
    print()
    
    # Test case 3
    nums3 = [1, 2]
    result3 = sol.permute(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [[1,2],[2,1]] (order may vary)")
    print()


if __name__ == "__main__":
    test_permutations()


"""
Key Takeaways:
- Permutations: ORDER MATTERS (unlike subsets/combinations)
- Use all elements exactly once (unlike combination sum where reuse allowed)
- Need to track which elements are already used (boolean array or set)
- Base case: when current permutation length equals input length
- Classic "choose, explore, unchoose" backtracking pattern
- n! permutations for n elements (factorial growth)

Common Mistakes to Avoid:
- Forgetting that order matters - [1,2] and [2,1] are DIFFERENT permutations
- Not properly tracking used elements (leads to duplicates or skipped permutations)
- Forgetting to backtrack (not unmarking used elements)
- Not copying the current permutation when adding to result
- Confusing with combinations (combinations don't care about order)

Pattern Recognition:
- Backtracking with "used" tracking
- Different from Subsets: must use ALL elements, order matters
- Different from Combinations: order matters, so [1,2] ≠ [2,1]
- Different from Combination Sum: use each element exactly once (no reuse)
- For loop explores all choices at current decision point
- Similar to: Permutations II (with duplicates), Letter Combinations, N-Queens
"""
