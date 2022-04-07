"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # assuming originally had conflicts

        # insert new interval first
        if not intervals:
            intervals = [newInterval]
        else:
            for i, interval in enumerate(intervals):
                start = interval[0]
                if newInterval[0] <= start:
                    intervals.insert(i, newInterval)
                    break
            intervals.append(newInterval)

        # now simply merge from LC-56
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.insert(input[0], input[1]) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    ([[1, 5]], [2, 7]),
    ([], [5, 7]),
    ([[1, 3], [6, 9]], [2, 5]),
    ([[1, 3], [6, 9]], [4, 5]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
]
expected = [
    [[1, 7]],
    [[5, 7]],
    [[1, 5], [6, 9]],
    [[1, 3], [4, 5], [6, 9]],
    [[1, 2], [3, 10], [12, 16]],
]


sol = Solution()
nums = [3, 2, 4]
target = 6
s = "A man, a plan, a canal: Panama"

sol.test(input, expected)
