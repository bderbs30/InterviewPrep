"""
Subsets II

Problem:
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- nums may contain duplicates

Link: https://leetcode.com/problems/subsets-ii/
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # Your code here
        pass























# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: Backtracking with Sorting and Skip Duplicates
    
    Time Complexity: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
    Space Complexity: O(n) - recursion depth
    
    Key Insight:
    - Similar to Subsets I, but we need to avoid duplicate subsets
    - Sort the array first so duplicates are adjacent
    - When backtracking, skip duplicate elements at the same level
    - Only skip if it's NOT the first occurrence in that recursive call
    - The trick: skip nums[i] if nums[i] == nums[i-1] AND nums[i-1] wasn't chosen
    '''
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        nums.sort()  # Sort to group duplicates together
        
        def backtrack(i):
            # Base case: reached end of array
            if i >= len(nums):
                result.append(subset[:])
                return
            
            # Decision 1: Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            
            # Decision 2: Exclude nums[i] (backtrack)
            subset.pop()
            
            # Skip duplicates: if we skip nums[i], skip all subsequent duplicates too
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)
        
        backtrack(0)
        return result


class Solution2:
    '''
    Approach 2: Backtracking with Explicit Duplicate Check
    
    Time Complexity: O(n * 2^n)
    Space Complexity: O(n)
    
    Key Insight:
    - Sort array to group duplicates
    - For each index, check if current element equals previous element
    - Only include current element if:
      1. It's the first element (i == 0), OR
      2. It's not equal to previous (nums[i] != nums[i-1]), OR
      3. Previous element was included (use a flag to track this)
    - Alternative: skip if nums[i] == nums[i-1] and we're at a decision point where
      we didn't include nums[i-1]
    '''
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        nums.sort()
        
        def backtrack(i, include_prev=False):
            if i >= len(nums):
                result.append(subset[:])
                return
            
            # Skip duplicates only if previous was NOT included
            if i > 0 and nums[i] == nums[i-1] and not include_prev:
                backtrack(i + 1, False)
                return
            
            # Include current
            subset.append(nums[i])
            backtrack(i + 1, True)
            
            # Exclude current
            subset.pop()
            backtrack(i + 1, False)
        
        backtrack(0, False)
        return result


class Solution3:
    '''
    Approach 3: Iterative with Duplicate Handling
    
    Time Complexity: O(n * 2^n)
    Space Complexity: O(1) - excluding output space
    
    Key Insight:
    - Similar to iterative approach for Subsets I
    - But need to handle duplicates carefully
    - When encountering a duplicate, only add it to subsets created in 
      the previous iteration (which included the duplicate)
    - Track which subsets to extend based on whether current num == previous num
    '''
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = [[]]
        start_idx = 0
        
        for i in range(len(nums)):
            # If current num is duplicate, only extend subsets from last iteration
            if i > 0 and nums[i] == nums[i-1]:
                prev_len = len(result)
                for j in range(start_idx, prev_len):
                    result.append(result[j] + [nums[i]])
                start_idx = prev_len
            else:
                # New number: extend all existing subsets
                start_idx = len(result)
                result += [subset + [nums[i]] for subset in result]
        
        return result


class Solution4:
    '''
    Approach 4: Set-based (Simpler but Less Efficient)
    
    Time Complexity: O(n * 2^n * n) - extra factor for set operations
    Space Complexity: O(n * 2^n) - for the set
    
    Key Insight:
    - Generate all subsets (can use Subsets I approach)
    - Use a set with tuples to track unique subsets
    - Sort each subset before adding to set
    - Convert back to list of lists
    - Less optimal due to set overhead, but conceptually simple
    '''
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []
        
        def backtrack(i):
            if i >= len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        
        # Remove duplicates using set of tuples
        seen = set()
        unique_result = []
        for sub in result:
            sub_tuple = tuple(sorted(sub))
            if sub_tuple not in seen:
                seen.add(sub_tuple)
                unique_result.append(sub)
        
        return unique_result
"""


# Test cases
def test_subsets_with_dup():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 2, 2]
    result1 = sol.subsetsWithDup(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[],[1],[1,2],[1,2,2],[2],[2,2]] (order may vary)")
    print()
    
    # Test case 2
    nums2 = [0]
    result2 = sol.subsetsWithDup(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [[],[0]]")
    print()
    
    # Test case 3
    nums3 = [1, 1, 2]
    result3 = sol.subsetsWithDup(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [[],[1],[1,1],[1,1,2],[1,2],[2]] (order may vary)")
    print()
    
    # Test case 4
    nums4 = [4, 4, 4, 1, 4]
    result4 = sol.subsetsWithDup(nums4)
    print(f"Input: {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: Should not contain duplicate subsets")
    print()


if __name__ == "__main__":
    test_subsets_with_dup()


"""
Key Takeaways:
- MUST sort array first to group duplicates together - this is critical!
- When excluding an element that's a duplicate, skip ALL subsequent duplicates at that level
- The key insight: if nums[i] == nums[i-1] and we didn't include nums[i-1], 
  then we shouldn't include nums[i] either (to avoid duplicate subsets)
- Pattern: "Skip duplicates if previous wasn't chosen" prevents duplicate subsets
- Different from Subsets I: need careful duplicate handling at decision points

Common Mistakes to Avoid:
- Not sorting the array first - duplicates won't be adjacent, harder to skip
- Including duplicate subsets because you didn't skip duplicates correctly
- Skipping duplicates even when previous duplicate WAS included (wrong logic)
- Forgetting that order doesn't matter: [1,2] == [2,1] for subset purposes
- Using set on unsorted subsets - [1,2] and [2,1] would be considered different

Pattern Recognition:
- Backtracking with duplicate handling
- Similar to: Subsets I (but with duplicates), Permutations II (similar duplicate skip pattern)
- Key technique: Sort + Skip duplicates at same decision level when previous wasn't chosen
- The duplicate skip logic: while nums[i] == nums[i+1] after excluding current
"""