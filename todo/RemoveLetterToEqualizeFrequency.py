# 2423. Remove Letter To Equalize Frequency
# Easy

# Description
# You are given a 0-indexed string word, consisting of lowercase English letters. 
# You need to select one index and remove the letter at that index from word so that 
# the frequency of every letter present in word is equal.

# Return true if it is possible to remove one letter so that the frequency of all 
# letters in word are equal, and false otherwise.

# Note:
# - The frequency of a letter x is the number of times it occurs in the string.
# - You must remove exactly one letter and cannot choose to do nothing.

# Example 1:
# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

# Example 2:
# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and the 
# frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

# Constraints:
# 2 <= word.length <= 100
# word consists of lowercase English letters only.


def equalFrequency(word: str) -> bool:
    """
    Determine if it's possible to remove exactly one letter from word so that 
    all remaining letters have equal frequency.
    
    Args:
        word: A string of lowercase English letters
    
    Returns:
        True if it's possible to remove one letter to equalize frequencies, False otherwise.
    """
    pass


# Test cases
def test_equalFrequency():
    # Example 1
    assert equalFrequency("abcc") == True, "Example 1 failed: 'abcc' should return True"
    
    # Example 2
    assert equalFrequency("aazz") == False, "Example 2 failed: 'aazz' should return False"
    
    # Additional test cases
    
    # All characters same frequency (1 each) - removing one makes all equal
    assert equalFrequency("abc") == True, "All unique chars should return True"
    
    # All characters same - removing one still leaves all equal
    assert equalFrequency("aa") == True, "Two same chars should return True"
    assert equalFrequency("aaa") == True, "Three same chars should return True"
    
    # One character appears once more than others
    assert equalFrequency("aabbc") == True, "Should return True (remove one 'c')"
    assert equalFrequency("aabbcc") == False, "Should return False"
    
    # One character appears twice more than others
    assert equalFrequency("aabbb") == True, "Should return True (remove one 'b')"
    
    # Multiple characters with different frequencies
    assert equalFrequency("aabbccd") == False, "Should return False"
    
    # Edge case: two characters, one appears once
    assert equalFrequency("ab") == True, "Two different chars should return True"
    
    # Edge case: all same character
    assert equalFrequency("aaaa") == True, "All same chars should return True"
    
    # Complex case: one extra character
    assert equalFrequency("aabbccc") == True, "Should return True (remove one 'c')"
    
    # Complex case: cannot equalize
    assert equalFrequency("aabbccdd") == False, "Should return False"
    
    # Case where removing one makes frequencies equal
    assert equalFrequency("abbcc") == True, "Should return True"
    
    # Case with many characters
    assert equalFrequency("abcdefghijklmnopqrstuvwxyz") == True, "All unique should return True"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_equalFrequency()


# Hints:
# 1. Count the frequency of each character in the word.
# 2. Try removing each character one by one and check if the remaining frequencies are equal.
# 3. After removing a character, check if all remaining frequencies are the same.
# 4. Consider edge cases: all characters are the same, all characters are unique, etc.
# 5. You can use a dictionary to count frequencies efficiently.
# 6. Think about what happens when you remove a character - its frequency decreases by 1.
# 7. If all frequencies are already equal, removing one character might still keep them equal (if count > 1).
# 8. If one character appears once more than all others, removing it will equalize frequencies.
# 9. If frequencies are like [n, n, n, n+1], removing one from the n+1 frequency makes all n.
# 10. If there's only one character with frequency 1 and all others have frequency n, removing that one makes all n.

