# ### Number of Islands
#
# Given a 2D grid where '1' represents land and '0' represents water,
# count and return the number of islands.
#
# An island is formed by connecting adjacent lands horizontally or vertically
# and is surrounded by water.
#
# You may assume water is surrounding the grid (i.e., all the edges are water).
#
# Example 1:
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# Output: 4
#
# Constraints:
# - 1 <= grid.length, grid[i].length <= 100
# - grid[i][j] is '0' or '1'


from typing import List
from collections import deque


def numberOfIslands(grid: List[List[str]]) -> int:

    count = 0
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(row, col):
        queue = deque([(row, col)])
        visited.add((row, col))

        while queue:
            curr_row, curr_col = queue.popleft()
            for dir_row, dir_col in dirs:
                new_row = curr_row + dir_row
                new_col = curr_col + dir_col
                if (
                    new_row >= 0
                    and new_row < rows
                    and new_col >= 0
                    and new_col < cols
                    and grid[new_row][new_col] == "1"
                    and (new_row, new_col) not in visited
                ):
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                bfs(row, col)
                count += 1

    return count


if __name__ == "__main__":
    grid1 = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(numberOfIslands(grid1))  # Expected: 1

    grid2 = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(numberOfIslands(grid2))  # Expected: 4
