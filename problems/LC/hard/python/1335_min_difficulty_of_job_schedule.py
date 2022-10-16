"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have
to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties
of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.



Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

Example 2:
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
"""


from functools import cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        basically divide array into d cuts with min sum

        DP problem

        Ex
        [6, 5, 4, 3, 2, 1], 2
        [0, 1, 2, 3, 4, 5]
        """
        n = len(jobDifficulty)

        # there are more days than jobs available
        if n < d:
            return -1

        # starting from the back calculate what the max number of everything to the right is
        # i.e., the max job on the last day is the last day, thats why we start from last - 1
        max_job_remaining = jobDifficulty[:]
        for i in range(n - 2, -1, -1):
            max_job_remaining[i] = max(max_job_remaining[i], max_job_remaining[i + 1])

        # memoizing the results
        @cache
        def dp(i, days_remaining):
            # if there's one day left, we check the max date from this day forward
            if days_remaining == 1:
                return max_job_remaining[i]

            #
            res = float("inf")
            daily_max_job = 0  # max job for breaking the day here

            for j in range(i, n - days_remaining + 1):
                daily_max_job = max(daily_max_job, jobDifficulty[j])
                res = min(res, daily_max_job + dp(j + 1, days_remaining - 1))

            return res

        return dp(0, d)

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.minDifficulty(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[7, 1, 7, 1, 7, 1], 3],
    [[6, 5, 4, 3, 2, 1], 2],
    [[9, 9, 9], 4],
    [[1, 1, 1], 3],
]
expected = [
    15,
    7,
    -1,
    3,
]


sol = Solution()
sol.test(input, expected)
