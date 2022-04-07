"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.merge(input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]],
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
]
expected = [
    [[1, 10]],
    [[1, 6], [8, 10], [15, 18]],
    [[1, 5]],
]


sol = Solution()
nums = [3, 2, 4]
target = 6
s = "A man, a plan, a canal: Panama"

sol.test(input, expected)
