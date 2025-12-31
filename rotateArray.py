# ### Rotate Array
#
# You are given an integer array nums, rotate the array to the right
# by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7,8], k = 4
# Output: [5,6,7,8,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
# rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
# rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
# rotate 4 steps to the right: [5,6,7,8,1,2,3,4]
#
# Example 2:
# Input: nums = [1000,2,4,-3], k = 2
# Output: [4,-3,1000,2]
# Explanation:
# rotate 1 steps to the right: [-3,1000,2,4]
# rotate 2 steps to the right: [4,-3,1000,2]
#
# Constraints:
# - 1 <= nums.length <= 100,000
# - -(2^31) <= nums[i] <= ((2^31)-1)
# - 0 <= k <= 100,000
#
# Note: Modify the array in-place with O(1) extra space.


from typing import List


def rotateArray(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n  # Handle k > n

    # Helper to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(0, n - 1)

    # Step 2: Reverse first k elements
    reverse(0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(k, n - 1)


if __name__ == "__main__":
    # Test 1
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    rotateArray(nums1, 4)
    print(nums1)  # Expected: [5, 6, 7, 8, 1, 2, 3, 4]

    # Test 2
    nums2 = [1000, 2, 4, -3]
    rotateArray(nums2, 2)
    print(nums2)  # Expected: [4, -3, 1000, 2]

    # Test 3: Edge case - k larger than array length
    nums3 = [1, 2, 3]
    rotateArray(nums3, 4)
    print(nums3)  # Expected: [3, 1, 2] (same as k=1)

    # Test 4: Edge case - k = 0
    nums4 = [1, 2, 3, 4]
    rotateArray(nums4, 0)
    print(nums4)  # Expected: [1, 2, 3, 4] (no change)
