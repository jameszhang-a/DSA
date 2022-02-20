from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort the list by start time
        # then traverse linearly
        intervals = sorted(intervals, key=lambda s: (s[0], -s[1]))
        print(intervals)
        count = 0
        prev = -1

        # since all intervals are sorted by earliest start and latest end,
        # the interval that comes before must be able to covered the next
        # as long as the end time of the earlier is later than the end time
        # of the next

        for int in intervals:
            if int[1] > prev:
                # Only count ones that aren't covered
                prev = int[1]
                count += 1

        return count


sol = Solution()
intervals = [[3, 10], [4, 10], [5, 11]]


print(sol.removeCoveredIntervals(intervals))
