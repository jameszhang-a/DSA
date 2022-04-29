"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


from itertools import product
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [float("inf")] * m

        for i, j in product(range(n), range(m)):
            if j == 0 and i == 0:
                dp[0] = grid[i][j]
            elif j == 0:
                dp[0] += grid[i][j]
            else:
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]

    def minPathSum_noSpace(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i, j in product(range(n), range(m)):
            if i > 0 and j > 0:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            elif i > 0:  # first column
                grid[i][j] += grid[i - 1][j]
            elif j > 0:  # first row
                grid[i][j] += grid[i][j - 1]

        return grid[-1][-1]

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.minPathSum_noSpace(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]],
    [[[1, 2, 3], [4, 5, 6]]],
]
expected = [
    7,
    12,
]


sol = Solution()
sol.test(input, expected)
