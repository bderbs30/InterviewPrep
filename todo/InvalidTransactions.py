# 1169. Invalid Transactions - LeetCode
# Problem Link: https://leetcode.com/problems/invalid-transactions/description/

# Description
# A transaction is possibly invalid if:
# 1. the amount exceeds $1000, or
# 2. if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

# You are given an array of strings transaction where transactions[i] consists of comma-separated values 
# representing the name, time (in minutes), amount, and city of the transaction.

# Return a list of transactions that are possibly invalid. You may return the answer in any order.

# Example 1:
# Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# Output: ["alice,20,800,mtv","alice,50,100,beijing"]
# Explanation: The first transaction is invalid because the second transaction occurs within a difference 
# of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

# Example 2:
# Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# Output: ["alice,50,1200,mtv"]

# Example 3:
# Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# Output: ["bob,50,1200,mtv"]

# Constraints:
# - transactions.length <= 1000
# - Each transactions[i] takes the form "{name},{time},{amount},{city}"
# - Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
# - Each {time} consist of digits, and represent an integer between 0 and 1000.
# - Each {amount} consist of digits, and represent an integer between 0 and 2000.


from typing import List


def invalidTransactions(transactions: List[str]) -> List[str]:
    """
    Identifies invalid transactions based on the given criteria.
    
    A transaction is invalid if:
    1. The amount exceeds $1000, OR
    2. It occurs within 60 minutes (inclusive) of another transaction 
       with the same name in a different city.
    
    Args:
        transactions: A list of transaction strings, each formatted as 
                      "name,time,amount,city"
    
    Returns:
        A list of invalid transactions (can be in any order).
    """
    result = []

    # we are given a list of tranactions and need to determine which
    # transactions are invalid 
    # to do this we need to check if the transaction amount exceeds 1000
    # if there is a transaction within 60 mins of this transaction
    # that has the same name but different city 

    # name, time, amount, city
    # we can use split to split on the comma to get a list to easily access
    # the various elements

    



        


# Test cases
def test_invalidTransactions():
    # Example 1 from problem description
    transactions1 = ["alice,20,800,mtv", "alice,50,100,beijing"]
    result1 = invalidTransactions(transactions1)
    # Both transactions are invalid (within 60 min, same name, different city)
    assert len(result1) == 2, f"Expected 2 invalid transactions, got {len(result1)}"
    assert "alice,20,800,mtv" in result1, "First transaction should be invalid"
    assert "alice,50,100,beijing" in result1, "Second transaction should be invalid"
    print("Test 1 passed: Both transactions invalid (same name, different city, within 60 min)")
    
    # Example 2 from problem description
    transactions2 = ["alice,20,800,mtv", "alice,50,1200,mtv"]
    result2 = invalidTransactions(transactions2)
    # Only second transaction is invalid (amount > 1000)
    assert len(result2) == 1, f"Expected 1 invalid transaction, got {len(result2)}"
    assert "alice,50,1200,mtv" in result2, "Transaction with amount > 1000 should be invalid"
    assert "alice,20,800,mtv" not in result2, "Transaction with amount <= 1000 should be valid"
    print("Test 2 passed: Only transaction with amount > 1000 is invalid")
    
    # Example 3 from problem description
    transactions3 = ["alice,20,800,mtv", "bob,50,1200,mtv"]
    result3 = invalidTransactions(transactions3)
    # Only second transaction is invalid (amount > 1000, different name so no conflict)
    assert len(result3) == 1, f"Expected 1 invalid transaction, got {len(result3)}"
    assert "bob,50,1200,mtv" in result3, "Transaction with amount > 1000 should be invalid"
    assert "alice,20,800,mtv" not in result3, "Valid transaction should not be in result"
    print("Test 3 passed: Only transaction with amount > 1000 is invalid (different names)")
    
    # Test case: No invalid transactions
    transactions4 = ["alice,20,800,mtv", "alice,50,100,mtv"]
    result4 = invalidTransactions(transactions4)
    # Both valid: same city, amounts <= 1000
    assert len(result4) == 0, f"Expected 0 invalid transactions, got {len(result4)}"
    print("Test 4 passed: All transactions valid (same city, amounts <= 1000)")
    
    # Test case: Amount exactly 1000 (should be valid)
    transactions5 = ["alice,20,1000,mtv"]
    result5 = invalidTransactions(transactions5)
    assert len(result5) == 0, f"Expected 0 invalid transactions, got {len(result5)}"
    print("Test 5 passed: Amount exactly 1000 is valid")
    
    # Test case: Amount 1001 (should be invalid)
    transactions6 = ["alice,20,1001,mtv"]
    result6 = invalidTransactions(transactions6)
    assert len(result6) == 1, f"Expected 1 invalid transaction, got {len(result6)}"
    assert "alice,20,1001,mtv" in result6, "Amount > 1000 should be invalid"
    print("Test 6 passed: Amount > 1000 is invalid")
    
    # Test case: Same name, different city, exactly 60 minutes apart
    transactions7 = ["alice,20,800,mtv", "alice,80,100,beijing"]
    result7 = invalidTransactions(transactions7)
    # 80 - 20 = 60 minutes (within 60 inclusive)
    assert len(result7) == 2, f"Expected 2 invalid transactions, got {len(result7)}"
    assert "alice,20,800,mtv" in result7, "Transaction should be invalid (60 min apart, different city)"
    assert "alice,80,100,beijing" in result7, "Transaction should be invalid (60 min apart, different city)"
    print("Test 7 passed: Transactions exactly 60 minutes apart with different cities are invalid")
    
    # Test case: Same name, different city, 61 minutes apart (should be valid)
    transactions8 = ["alice,20,800,mtv", "alice,81,100,beijing"]
    result8 = invalidTransactions(transactions8)
    # 81 - 20 = 61 minutes (more than 60, so valid)
    assert len(result8) == 0, f"Expected 0 invalid transactions, got {len(result8)}"
    print("Test 8 passed: Transactions 61 minutes apart are valid")
    
    # Test case: Multiple transactions, complex scenario
    transactions9 = [
        "alice,20,800,mtv",      # Valid
        "alice,50,100,beijing",  # Invalid (within 60 min of first, different city)
        "bob,30,1200,mtv",       # Invalid (amount > 1000)
        "bob,90,100,mtv",        # Valid
        "charlie,10,500,nyc",    # Valid
        "charlie,70,600,nyc"     # Valid (same city)
    ]
    result9 = invalidTransactions(transactions9)
    assert len(result9) == 2, f"Expected 2 invalid transactions, got {len(result9)}"
    assert "alice,50,100,beijing" in result9, "Should be invalid (within 60 min, different city)"
    assert "bob,30,1200,mtv" in result9, "Should be invalid (amount > 1000)"
    print("Test 9 passed: Complex scenario with multiple transactions")
    
    # Test case: Transaction invalid for both reasons
    transactions10 = ["alice,20,1200,mtv", "alice,50,100,beijing"]
    result10 = invalidTransactions(transactions10)
    # First: amount > 1000
    # Second: within 60 min, same name, different city
    # Both should be invalid
    assert len(result10) == 2, f"Expected 2 invalid transactions, got {len(result10)}"
    assert "alice,20,1200,mtv" in result10, "Should be invalid (amount > 1000)"
    assert "alice,50,100,beijing" in result10, "Should be invalid (within 60 min, different city)"
    print("Test 10 passed: Transaction invalid for multiple reasons")
    
    # Test case: Same name, same city, within 60 minutes (should be valid)
    transactions11 = ["alice,20,800,mtv", "alice,50,100,mtv"]
    result11 = invalidTransactions(transactions11)
    assert len(result11) == 0, f"Expected 0 invalid transactions, got {len(result11)}"
    print("Test 11 passed: Same city transactions are valid even if within 60 minutes")
    
    # Test case: Edge case - single transaction with amount > 1000
    transactions12 = ["alice,0,1500,mtv"]
    result12 = invalidTransactions(transactions12)
    assert len(result12) == 1, f"Expected 1 invalid transaction, got {len(result12)}"
    assert "alice,0,1500,mtv" in result12, "Single transaction with amount > 1000 should be invalid"
    print("Test 12 passed: Single transaction with amount > 1000")
    
    # Test case: Edge case - single transaction with amount <= 1000
    transactions13 = ["alice,0,500,mtv"]
    result13 = invalidTransactions(transactions13)
    assert len(result13) == 0, f"Expected 0 invalid transactions, got {len(result13)}"
    print("Test 13 passed: Single transaction with amount <= 1000")
    
    # Test case: Multiple transactions with same name, different times and cities
    transactions14 = [
        "alice,10,800,mtv",      # Valid
        "alice,20,100,beijing",  # Invalid (within 60 min, different city)
        "alice,100,200,mtv",     # Valid (more than 60 min from others)
        "alice,150,300,nyc"      # Valid (more than 60 min from others)
    ]
    result14 = invalidTransactions(transactions14)
    assert len(result14) == 2, f"Expected 2 invalid transactions, got {len(result14)}"
    assert "alice,10,800,mtv" in result14, "Should be invalid (within 60 min of second, different city)"
    assert "alice,20,100,beijing" in result14, "Should be invalid (within 60 min of first, different city)"
    print("Test 14 passed: Multiple transactions with same name")
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    test_invalidTransactions()

