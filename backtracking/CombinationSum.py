"""
Combination Sum

Problem:
You are given an array of distinct integers nums and a target integer target. 
Your task is to return a list of all unique combinations of nums where the chosen 
numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations 
are the same if the frequency of each of the chosen numbers is the same, otherwise 
they are different.

You may return the combinations in any order and the order of the numbers in each 
combination can be in any order.

Example 1:
Input: nums = [2,5,6,9], target = 9
Output: [[2,2,5],[9]]
Explanation: 
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:
Input: nums = [3,4,5], target = 16
Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
Input: nums = [3], target = 5
Output: []

Constraints:
- All elements of nums are distinct
- 1 <= nums.length <= 20
- 2 <= nums[i] <= 30
- 2 <= target <= 30

Link: https://neetcode.io/problems/combination-target-sum/question?list=neetcode150
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Your code here
        pass





























# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: Backtracking with Index
    
    Time Complexity: O(2^(t/m)) where t is target, m is minimum value in nums
    Space Complexity: O(t/m) - recursion depth (max elements needed to reach target)
    
    Key Insight:
    - At each position, we can choose to include a number multiple times
    - Use index to avoid duplicates (only explore numbers from current index onwards)
    - Track running sum and stop when sum == target or sum > target
    - Can reuse same number, so don't increment index when choosing to include
    '''
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(i, curr, total):
            # Base case: found valid combination
            if total == target:
                result.append(curr[:])
                return
            
            # Base case: exceeded target or out of numbers
            if total > target or i >= len(nums):
                return
            
            # Decision 1: Include nums[i] (can use again, so stay at index i)
            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()
            
            # Decision 2: Skip nums[i] (move to next index)
            backtrack(i + 1, curr, total)
        
        backtrack(0, [], 0)
        return result


class Solution2:
    '''
    Approach 2: Backtracking with For Loop
    
    Time Complexity: O(2^(t/m))
    Space Complexity: O(t/m)
    
    Key Insight:
    - Use a for loop to iterate through choices at each level
    - Start from current index to avoid duplicates
    - Since we can reuse elements, pass same index to next recursion
    - More intuitive for some people - explores all choices explicitly
    '''
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(start, curr, total):
            if total == target:
                result.append(curr[:])
                return
            
            if total > target:
                return
            
            # Try each number from start index onwards
            for i in range(start, len(nums)):
                curr.append(nums[i])
                # Pass i (not i+1) because we can reuse same element
                backtrack(i, curr, total + nums[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return result


class Solution3:
    '''
    Approach 3: Optimized with Sorting
    
    Time Complexity: O(n log n + 2^(t/m)) - sorting + backtracking
    Space Complexity: O(t/m)
    
    Key Insight:
    - Sort array first to enable early pruning
    - Once a number exceeds remaining target, all larger numbers will too
    - Can break early from for loop instead of continuing
    - Slight optimization but same worst-case complexity
    '''
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()  # Sort for early termination
        result = []
        
        def backtrack(start, curr, total):
            if total == target:
                result.append(curr[:])
                return
            
            for i in range(start, len(nums)):
                # Early termination: if current number is too large, rest will be too
                if total + nums[i] > target:
                    break
                
                curr.append(nums[i])
                backtrack(i, curr, total + nums[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return result
"""


# Test cases
def test_combination_sum():
    sol = Solution()
    
    # Test case 1
    nums1 = [2, 5, 6, 9]
    target1 = 9
    result1 = sol.combinationSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print(f"Expected: [[2,2,5],[9]] (order may vary)")
    print()
    
    # Test case 2
    nums2 = [3, 4, 5]
    target2 = 16
    result2 = sol.combinationSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print(f"Expected: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]] (order may vary)")
    print()
    
    # Test case 3
    nums3 = [3]
    target3 = 5
    result3 = sol.combinationSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print(f"Expected: []")
    print()
    
    # Test case 4 - edge case: target equals one element
    nums4 = [2, 3, 6, 7]
    target4 = 7
    result4 = sol.combinationSum(nums4, target4)
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")
    print(f"Expected: [[2,2,3],[7]] (order may vary)")
    print()


if __name__ == "__main__":
    test_combination_sum()


"""
Key Takeaways:
- Can reuse same element unlimited times -> stay at same index when including
- Use index parameter to avoid duplicate combinations (always move forward)
- Track running sum to know when to stop (sum == target or sum > target)
- Three base cases: found solution (sum == target), exceeded (sum > target), no more options (i >= len)
- Sorting enables early termination optimization but doesn't change worst-case complexity

Common Mistakes to Avoid:
- Moving to i+1 when including element (we can reuse, so stay at i)
- Not tracking the running sum (causes unnecessary recursion)
- Forgetting to copy the current combination when appending to result
- Not handling the case where sum exceeds target (infinite recursion)
- Trying to avoid duplicates by using a set (index approach is more efficient)

Pattern Recognition:
- Backtracking with "unlimited reuse" variant
- Key difference from Subsets: can use same element multiple times
- Key difference from Permutations: order doesn't matter (use index to prevent duplicates)
- Track accumulated value (sum) to determine when to stop
- Similar to: Combination Sum II (each element used once), Combination Sum III (fixed k elements)
"""
