"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move to either index i
or index i + 1 on the next row.



Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""
from typing import List

from itertools import product


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]

        for i in reversed(range(n - 1)):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.minimumTotal(*input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]],
    [[[-10]]],
]
expected = [
    11,
    -10,
]


sol = Solution()

sol.test(input, expected)
