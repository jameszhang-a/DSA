"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
import itertools
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # incase the entrance is blocked
        if grid[0][0] == 1:
            return 0

        # set all blocks as -1
        for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 1:
                grid[i][j] = -1

        # initialize first row
        grid[0][0] = 1
        for i in range(1, len(grid[0])):
            grid[0][i] = 1 if grid[0][i] != -1 and grid[0][i - 1] > 0 else 0

        # dp step
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = 0
                    continue

                if j > 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                else:
                    grid[i][j] = grid[i - 1][j]

        # print(f"{grid = }")
        return grid[-1][-1]

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.uniquePathsWithObstacles(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[[0, 1], [0, 0]]],
    [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]],
]
expected = [
    1,
    2,
]


sol = Solution()
sol.test(input, expected)
