"""
Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

from tkinter import N
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Bottom up approach filling up matrix of [len(nums)][sum(nums)/2]
        """
        # Total sum must be even, thus the half must be an int
        if (goal := sum(nums)) % 2 != 0:
            return False

        n = len(nums)
        goal = int(goal / 2 + 1)
        dp = [[False] * (goal) for _ in range(n)]

        # first of all, all 0 sum is possible
        for i in range(n):
            dp[i][0] = True

        # for first row, only 1 element to worry about
        if nums[0] < goal:
            dp[0][nums[0]] = True

        # actual dp step
        for i in range(1, n):
            for j in range(1, goal):
                last_val = nums[: i + 1][-1]

                without_new = dp[i - 1][j]
                with_new = dp[i - 1][j - last_val] if j - last_val >= 0 else False

                dp[i][j] = without_new or with_new

        return dp[n - 1][goal - 1]

    def partitionOptimized(self, nums: List[int]) -> bool:
        # total must be even
        if (goal := sum(nums)) % 2 != 0:
            return False

        # need to reach half of the sum
        goal //= 2
        n = len(nums)
        dp = [False for _ in range(goal + 1)]

        # 0 sum is always possible
        dp[0] = True

        for i in range(n):
            next = nums[i]
            for j in range(goal, next - 1, -1):
                dp[j] = dp[j] or dp[j - next]

        return dp[goal]

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.partitionOptimized(input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


s = Solution()
input = [
    [1, 5, 11, 5],
    [1, 2, 3, 5],
    [1, 2, 3, 4],
    [1, 1, 3, 4, 7],
    [2, 3, 4, 6],
    [100],
    [1],
]
expected = [True, False, True, True, False, False, False]


# print(s.canPartition(n))
s.test(input, expected)
