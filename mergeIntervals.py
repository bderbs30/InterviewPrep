# ### Merge Intervals
#
# Given an array of intervals where intervals[i] = [start_i, end_i],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.
#
# You may return the answer in any order.
#
# Note: Intervals are non-overlapping if they have no common point.
# For example, [1, 2] and [3, 4] are non-overlapping,
# but [1, 2] and [2, 3] are overlapping.
#
# Example 1:
# Input: intervals = [[1,3],[1,5],[6,7]]
# Output: [[1,5],[6,7]]
#
# Example 2:
# Input: intervals = [[1,2],[2,3]]
# Output: [[1,3]]
#
# Constraints:
# - 1 <= intervals.length <= 1000
# - intervals[i].length == 2
# - 0 <= start <= end <= 1000


from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda interval: interval[0])

    result = [intervals[0]]  # Start with first interval

    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = result[-1]  # The last interval in result

        curr_start = current[0]
        curr_end = current[1]
        last_merged_end = last_merged[1]

        if curr_start <= last_merged_end:
            # Merge: update the end of last_merged
            result[-1][1] = max(last_merged_end, curr_end)
        else:
            # No overlap: add current as a new interval
            result.append(current)

    return result


if __name__ == "__main__":
    # Test 1
    intervals1 = [[1, 3], [1, 5], [6, 7]]
    print(mergeIntervals(intervals1))  # Expected: [[1, 5], [6, 7]]

    # Test 2
    intervals2 = [[1, 2], [2, 3]]
    print(mergeIntervals(intervals2))  # Expected: [[1, 3]]

    # Test 3: Already non-overlapping
    intervals3 = [[1, 2], [4, 5], [7, 8]]
    print(mergeIntervals(intervals3))  # Expected: [[1, 2], [4, 5], [7, 8]]

    # Test 4: All overlapping
    intervals4 = [[1, 4], [2, 5], [3, 6]]
    print(mergeIntervals(intervals4))  # Expected: [[1, 6]]
