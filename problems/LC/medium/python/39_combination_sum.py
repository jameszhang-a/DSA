"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations
for the given input.



Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 500
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtracking
        for each number:
            add it to temp_sum or not

            if temp_sum < target, add it

        """
        res = []

        def dfs(i, cur_sum, cmb):
            if cur_sum == target:
                res.append(cmb)
                return

            # too large or reach end of list
            if cur_sum > target or i == len(candidates):
                return

            for j in range(i, len(candidates)):
                curr_candidate = candidates[j]
                dfs(j, cur_sum + curr_candidate, cmb + [curr_candidate])

        dfs(0, 0, [])
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.combinationSum(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[2, 3, 6, 7], 7],
    [[2, 3, 5, 8], 8],
    [[2, 3, 5], 8],
    [[2, 3], 6],
]
expected = [
    [[2, 2, 3], [7]],
    [[2, 2, 2, 2], [2, 3, 3], [3, 5], [8]],
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    [[2, 2, 2], [3, 3]],
]


sol = Solution()
sol.test(input, expected)
