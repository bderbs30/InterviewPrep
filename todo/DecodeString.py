# Decode String
# You are given an encoded string s, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. There will not be input like 3a, 2[4], a[a] or a[2].

# The test cases are generated so that the length of the output will never exceed 100,000.

# Example 1:

# Input: s = "2[a3[b]]c"

# Output: "abbbabbbc"
# Example 2:

# Input: s = "axb3[z]4[c]"

# Output: "axbzzzcccc"
# Example 3:

# Input: s = "ab2[c]3[d]1[x]"

# Output: "abccdddx"
# Constraints:

# 1 <= s.length <= 30
# s is made up of lowercase English letters, digits, and square brackets '[]'.
# All the integers in s are in the range [1, 300].
# s is guaranteed to be a valid input.


def decodeString(s: str) -> str:
    """
    Decode an encoded string where k[encoded_string] means the encoded_string 
    is repeated k times.
    
    Args:
        s: Encoded string with format k[encoded_string]
    
    Returns:
        Decoded string
    """
    pass


# Test cases
def test_decodeString():
    # Example 1
    assert decodeString("2[a3[b]]c") == "abbbabbbc", "Example 1 failed"
    
    # Example 2
    assert decodeString("axb3[z]4[c]") == "axbzzzcccc", "Example 2 failed"
    
    # Example 3
    assert decodeString("ab2[c]3[d]1[x]") == "abccdddx", "Example 3 failed"
    
    # Additional test cases
    # Simple case: single bracket
    assert decodeString("3[a]") == "aaa", "Simple case failed"
    
    # Nested brackets
    assert decodeString("2[3[a]]") == "aaaaaa", "Nested brackets failed"
    
    # Multiple separate brackets
    assert decodeString("2[a]2[b]") == "aabb", "Multiple brackets failed"
    
    # Single character with brackets
    assert decodeString("a2[b]c") == "abbc", "Mixed case failed"
    
    # Deep nesting
    assert decodeString("2[a2[b2[c]]]") == "abccbccabccbcc", "Deep nesting failed"
    
    # Single repetition
    assert decodeString("1[a]") == "a", "Single repetition failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_decodeString()