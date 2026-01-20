"""
Climbing Stairs

Problem:
You are given an integer `n` representing the number of steps to reach the top of a staircase. 
You can climb with either `1` or `2` steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:
1. 1 + 1 = 2
2. 2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1. 1 + 1 + 1 = 3
2. 1 + 2 = 3
3. 2 + 1 = 3

Constraints:
- 1 <= n <= 30

Link: https://neetcode.io/problems/climbing-stairs/question
"""


# ============================================================
# YOUR SOLUTION - Write your code here
# ============================================================

class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)


# ============================================================
# SOLUTION APPROACHES (Commented out - uncomment after solving)
# ============================================================

"""
class Solution1:
    '''
    Approach 1: Recursive DFS (Your Current Solution)
    
    Time Complexity: O(2^n) - exponential, each step branches into 2 choices
    Space Complexity: O(n) - recursion stack depth
    
    Key Insight:
    - At each step i, we have two choices: take 1 step or 2 steps
    - We count ALL paths by adding results from both choices
    - Base case: `return i == n` uses Python's boolean arithmetic:
      * `True` (when i == n) is treated as `1` in addition
      * `False` (when i > n) is treated as `0` in addition
    - This is essentially counting all paths in a decision tree
    '''
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n  # True→1 if reached exactly, False→0 if overshot
            return dfs(i + 1) + dfs(i + 2)  # Sum of paths from both choices
        
        return dfs(0)


class Solution2:
    '''
    Approach 2: Memoization (Top-Down DP)
    
    Time Complexity: O(n) - each subproblem solved once
    Space Complexity: O(n) - memo cache + recursion stack
    
    Key Insight:
    - Same recursive structure but cache results to avoid recomputation
    - Many subproblems are solved multiple times in naive recursion
    - Memoization eliminates redundant work
    '''
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n:
                result = 1 if i == n else 0
            else:
                result = dfs(i + 1) + dfs(i + 2)
            memo[i] = result
            return result
        
        return dfs(0)


class Solution3:
    '''
    Approach 3: Bottom-Up DP (Iterative)
    
    Time Complexity: O(n)
    Space Complexity: O(n) - can be optimized to O(1)
    
    Key Insight:
    - Build solution from base cases up
    - dp[i] = number of ways to reach step i
    - To reach step i, you can come from step i-1 or step i-2
    - dp[i] = dp[i-1] + dp[i-2] (Fibonacci pattern!)
    '''
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to reach step 1
        dp[2] = 2  # Two ways to reach step 2: (1+1) or (2)
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


class Solution4:
    '''
    Approach 4: Space-Optimized Bottom-Up DP
    
    Time Complexity: O(n)
    Space Complexity: O(1) - only store last two values
    
    Key Insight:
    - We only need the last two values, not entire array
    - This is essentially computing Fibonacci numbers
    - Pattern: f(n) = f(n-1) + f(n-2) where f(1)=1, f(2)=2
    '''
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2 = 1  # Ways to reach step 1
        prev1 = 2  # Ways to reach step 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1
"""


# Test cases
def test_climb_stairs():
    sol = Solution()
    
    # Test case 1
    n1 = 2
    result1 = sol.climbStairs(n1)
    print(f"Input: n = {n1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print()
    
    # Test case 2
    n2 = 3
    result2 = sol.climbStairs(n2)
    print(f"Input: n = {n2}")
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print()
    
    # Test case 3
    n3 = 4
    result3 = sol.climbStairs(n3)
    print(f"Input: n = {n3}")
    print(f"Output: {result3}")
    print(f"Expected: 5")
    print()
    
    # Test case 4
    n4 = 5
    result4 = sol.climbStairs(n4)
    print(f"Input: n = {n4}")
    print(f"Output: {result4}")
    print(f"Expected: 8")
    print()


if __name__ == "__main__":
    test_climb_stairs()


"""
=== DETAILED TRACE EXPLANATION ===

Understanding the Base Case: `return i == n`

This is a Python boolean arithmetic trick! Here's how it works:

- `i == n` returns a boolean: `True` if equal, `False` otherwise
- In Python, booleans are automatically converted to integers in arithmetic:
  - `True` becomes `1`
  - `False` becomes `0`
- So `return i == n` is equivalent to: `return 1 if i == n else 0`

Examples:
- If i=3, n=3: `i == n` → `True` → treated as `1` in addition
- If i=4, n=3: `i == n` → `False` → treated as `0` in addition

This allows us to:
- Return 1 when we've reached the target (i == n) - count this as a valid path
- Return 0 when we've overshot (i > n) - don't count this path
- Use the result directly in addition: `dfs(i+1) + dfs(i+2)` works perfectly!

Alternative (more explicit) base case:
```python
if i >= n:
    return 1 if i == n else 0
```
But `return i == n` is more concise and Pythonic!

---

Why do we return dfs(i + 1) + dfs(i + 2)?

The key insight: We're COUNTING all possible paths, not choosing one path.
At each step, we have TWO independent choices, and we want to count paths from BOTH.

Let's trace through n = 3:

Call: dfs(0) - We're at step 0, need to reach step 3
├─ Choice 1: Take 1 step → dfs(1)
│  ├─ Choice 1: Take 1 step → dfs(2)
│  │  ├─ Choice 1: Take 1 step → dfs(3) → returns 1 (i == n)
│  │  └─ Choice 2: Take 2 steps → dfs(4) → returns 0 (i > n)
│  │  └─ dfs(2) = 1 + 0 = 1
│  └─ Choice 2: Take 2 steps → dfs(3) → returns 1 (i == n)
│  └─ dfs(1) = 1 + 1 = 2
└─ Choice 2: Take 2 steps → dfs(2)
   ├─ Choice 1: Take 1 step → dfs(3) → returns 1 (i == n)
   └─ Choice 2: Take 2 steps → dfs(4) → returns 0 (i > n)
   └─ dfs(2) = 1 + 0 = 1

dfs(0) = dfs(1) + dfs(2) = 2 + 1 = 3 ✓

Visual Representation:
Step 0 → Step 1 → Step 2 → Step 3  (Path 1: 1+1+1)
Step 0 → Step 1 → Step 3          (Path 2: 1+2)
Step 0 → Step 2 → Step 3          (Path 3: 2+1)

Why ADD instead of choosing one?
- We're not asking "which path should I take?"
- We're asking "how many different paths exist?"
- Each choice creates a separate path, so we count ALL of them
- Adding dfs(i+1) + dfs(i+2) sums up all valid paths from both branches

Think of it like a BINARY DECISION TREE:
      dfs(0) = 3
     /        \
  dfs(1) = 2  dfs(2) = 1
  /    \      /    \
dfs(2) dfs(3) dfs(3) dfs(4)
  |     |     |     |
  1     1     1     0

Tree Structure:
- Each node = "How many ways from step i to reach step n?"
- Left child = Take 1 step → dfs(i+1)
- Right child = Take 2 steps → dfs(i+2)
- Leaf nodes = Base cases (i >= n, return 1 or 0)
- Internal nodes = Sum of left subtree + right subtree

We sum subtrees (post-order traversal):
- dfs(2) = dfs(3) + dfs(4) = 1 + 0 = 1 (left subtree + right subtree)
- dfs(1) = dfs(2) + dfs(3) = 1 + 1 = 2 (left subtree + right subtree)
- dfs(0) = dfs(1) + dfs(2) = 2 + 1 = 3 (left subtree + right subtree)

This is exactly like counting all root-to-leaf paths where leaves with value 1 are valid solutions!

Key Takeaways:
- This is a COUNTING problem, not an OPTIMIZATION problem
- We add because we want the total count of all valid paths
- Each recursive call returns the number of ways from that position to reach n
- IMPORTANT: We only return 1 when we reach exactly n (i == n)
- Intermediate steps (like step 2) return the COUNT of paths from that step to n, not 1
- The sum represents: "ways if I take 1 step" + "ways if I take 2 steps"
- This creates a Fibonacci-like pattern: f(n) = f(n-1) + f(n-2)

Common Mistakes to Avoid:
- Returning max(dfs(i+1), dfs(i+2)) - This would find ONE path, not count ALL paths
- Returning dfs(i+1) or dfs(i+2) - This would only explore one branch
- Not understanding that we're counting, not optimizing

Pattern Recognition:
- Dynamic Programming - Counting Paths variant
- Fibonacci sequence: f(n) = f(n-1) + f(n-2)
- Binary decision tree where we sum left and right subtrees
- Each node = count of paths from that step to target
- Post-order traversal: process children, then sum their results
- Can be optimized with memoization or bottom-up DP

---

=== OPTIMIZATION STRATEGIES ===

The Problem with Naive Recursion:
- We recompute the same subproblems multiple times
- Example: For n=5, dfs(3) is called 3 times, dfs(4) is called 5 times
- This leads to O(2^n) time complexity

Optimization 1: Memoization (Top-Down DP)
- Key insight: "We know what the previous values were"
- Cache results when first computed: memo[i] = result
- Check cache before computing: if i in memo: return memo[i]
- Each subproblem computed ONCE, then reused
- Time: O(n) - each step computed once
- Space: O(n) - memo cache + recursion stack

Optimization 2: Bottom-Up DP
- Key insight: "We only need the previous 2 values"
- Build from base cases up (step n → step 0)
- Use array: dp[i] = dp[i+1] + dp[i+2]
- Start with known values: dp[n] = 1, dp[n-1] = 1
- Time: O(n) - single pass
- Space: O(n) - dp array

Optimization 3: Space-Optimized (Fibonacci Pattern!)
- Key insight: "We only need the LAST 2 values at any time"
- Like Fibonacci: f(n) = f(n-1) + f(n-2)
- Only keep: prev2 (i+2) and prev1 (i+1)
- Update: current = prev1 + prev2, then shift: prev2 = prev1, prev1 = current
- Time: O(n) - single pass
- Space: O(1) - only 2 variables!

Optimization Progression:
Naive (O(2^n)) → Memoization (O(n) time, O(n) space) 
                → Bottom-Up (O(n) time, O(n) space)
                → Space-Optimized (O(n) time, O(1) space)

The Fibonacci Connection:
- This problem is essentially: "What's the (n+1)th Fibonacci number?"
- f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5, f(5) = 8...
- Pattern: f(n) = f(n-1) + f(n-2) where f(0)=1, f(1)=1
"""