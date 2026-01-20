# 380. Insert Delete Get Random O(1) - Explanation
# Problem Link

# Description
# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.

# Example 1:

# Input: ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]

# Output: [null, true, false, true, 2, true, false, 2]
# Explanation:
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

# Constraints:

# -((2^31)-1) <= val <= ((2^31)-1)
# At most 2,00,000 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.


class RandomizedSet:
    """
    A data structure that supports insert, remove, and getRandom operations
    all in average O(1) time complexity.
    """
    
    def __init__(self):
        """
        Initializes the RandomizedSet object.
        """
        pass
    
    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present.
        
        Args:
            val: The value to insert
        
        Returns:
            True if the item was not present and inserted, False otherwise.
        """
        pass
    
    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present.
        
        Args:
            val: The value to remove
        
        Returns:
            True if the item was present and removed, False otherwise.
        """
        pass
    
    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements.
        Each element has the same probability of being returned.
        
        Returns:
            A random element from the set (guaranteed at least one element exists).
        """
        pass


# Test cases
def test_randomizedSet():
    # Example 1 from problem description
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(1) == True, "Insert 1 should return True"
    assert randomizedSet.remove(2) == False, "Remove 2 should return False (not present)"
    assert randomizedSet.insert(2) == True, "Insert 2 should return True"
    
    # getRandom should return either 1 or 2
    random_val = randomizedSet.getRandom()
    assert random_val in [1, 2], f"getRandom should return 1 or 2, got {random_val}"
    
    assert randomizedSet.remove(1) == True, "Remove 1 should return True"
    assert randomizedSet.insert(2) == False, "Insert 2 should return False (already present)"
    
    # After removing 1, getRandom should always return 2
    assert randomizedSet.getRandom() == 2, "getRandom should return 2 (only element)"
    
    # Additional test cases
    rs = RandomizedSet()
    
    # Test insert multiple values
    assert rs.insert(10) == True, "Insert 10 should return True"
    assert rs.insert(20) == True, "Insert 20 should return True"
    assert rs.insert(30) == True, "Insert 30 should return True"
    
    # Test inserting duplicate
    assert rs.insert(10) == False, "Insert duplicate 10 should return False"
    
    # Test remove existing value
    assert rs.remove(20) == True, "Remove 20 should return True"
    
    # Test remove non-existing value
    assert rs.remove(99) == False, "Remove 99 should return False (not present)"
    
    # Test getRandom returns valid value
    random_val = rs.getRandom()
    assert random_val in [10, 30], f"getRandom should return 10 or 30, got {random_val}"
    
    # Test with single element
    rs2 = RandomizedSet()
    assert rs2.insert(5) == True, "Insert 5 should return True"
    assert rs2.getRandom() == 5, "getRandom with single element should return 5"
    
    # Test remove and reinsert
    assert rs2.remove(5) == True, "Remove 5 should return True"
    assert rs2.insert(5) == True, "Re-insert 5 should return True"
    assert rs2.getRandom() == 5, "getRandom should return 5"
    
    # Test with negative numbers
    rs3 = RandomizedSet()
    assert rs3.insert(-1) == True, "Insert -1 should return True"
    assert rs3.insert(-2) == True, "Insert -2 should return True"
    random_val = rs3.getRandom()
    assert random_val in [-1, -2], f"getRandom should return -1 or -2, got {random_val}"
    
    # Test with zero
    rs4 = RandomizedSet()
    assert rs4.insert(0) == True, "Insert 0 should return True"
    assert rs4.getRandom() == 0, "getRandom should return 0"
    
    # Test multiple operations sequence
    rs5 = RandomizedSet()
    assert rs5.insert(1) == True
    assert rs5.insert(2) == True
    assert rs5.insert(3) == True
    assert rs5.remove(2) == True
    assert rs5.insert(4) == True
    random_val = rs5.getRandom()
    assert random_val in [1, 3, 4], f"getRandom should return 1, 3, or 4, got {random_val}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_randomizedSet()