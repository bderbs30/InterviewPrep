# 14. Longest Common Prefix
# Easy

# Description
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.


def longestCommonPrefix(strs: list[str]) -> str:
    """
    Find the longest common prefix string amongst an array of strings.
    
    Args:
        strs: A list of strings
    
    Returns:
        The longest common prefix string, or empty string if no common prefix exists.
    """
    pass


# Test cases
def test_longestCommonPrefix():
    # Example 1
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl", "Example 1 failed"
    
    # Example 2
    assert longestCommonPrefix(["dog", "racecar", "car"]) == "", "Example 2 failed"
    
    # Additional test cases
    
    # Single string
    assert longestCommonPrefix(["flower"]) == "flower", "Single string should return itself"
    
    # Empty array (edge case - though constraints say length >= 1)
    # This test is for robustness
    assert longestCommonPrefix([""]) == "", "Single empty string should return empty"
    
    # All strings identical
    assert longestCommonPrefix(["abc", "abc", "abc"]) == "abc", "All identical strings should return the string"
    
    # One string is prefix of others
    assert longestCommonPrefix(["ab", "abc", "abcd"]) == "ab", "One string is prefix of others"
    
    # No common prefix
    assert longestCommonPrefix(["abc", "def", "ghi"]) == "", "No common prefix should return empty"
    
    # Common prefix is single character
    assert longestCommonPrefix(["a", "ab", "abc"]) == "a", "Single character prefix"
    
    # Empty strings in array
    assert longestCommonPrefix(["", "b"]) == "", "Empty string in array should return empty"
    
    # All empty strings
    assert longestCommonPrefix(["", "", ""]) == "", "All empty strings should return empty"
    
    # Very short strings
    assert longestCommonPrefix(["a", "a"]) == "a", "Two single 'a' should return 'a'"
    assert longestCommonPrefix(["a", "b"]) == "", "Different single chars should return empty"
    
    # Long strings with common prefix
    assert longestCommonPrefix(["preface", "prefix", "prefer"]) == "pre", "Long strings with common prefix"
    
    # One character difference
    assert longestCommonPrefix(["abc", "abd", "abe"]) == "ab", "One character difference"
    
    # Different lengths, common prefix
    assert longestCommonPrefix(["leetcode", "leet", "leeds"]) == "lee", "Different lengths with common prefix"
    
    # First string is shortest
    assert longestCommonPrefix(["a", "ab", "abc"]) == "a", "First string is shortest"
    
    # Last string is shortest
    assert longestCommonPrefix(["abc", "ab", "a"]) == "a", "Last string is shortest"
    
    # Middle string is shortest
    assert longestCommonPrefix(["abc", "a", "abcd"]) == "a", "Middle string is shortest"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_longestCommonPrefix()


# Hints:
# 1. Start by comparing characters at the same index across all strings.
# 2. The common prefix can be at most as long as the shortest string in the array.
# 3. You can iterate character by character and check if all strings have the same character at that position.
# 4. If any string is empty, the common prefix is automatically empty.
# 5. Consider using the first string as a reference and compare other strings against it.
# 6. You can use Python's zip() function to iterate through characters at the same index across strings.
# 7. Stop as soon as you find a character mismatch or reach the end of the shortest string.
# 8. Think about edge cases: single string, empty strings, all strings identical, no common prefix.
# 9. A simple approach: find the shortest string first, then check if it's a prefix of all other strings.
# 10. Alternative approach: sort the array and compare only the first and last strings (they'll have the most different prefixes).
# 11. You can use string slicing to check if a prefix exists in all strings.
# 12. Consider using all() function with a generator expression to check if all strings have the same character at an index.

