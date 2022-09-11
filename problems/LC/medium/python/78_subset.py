"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]



Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        subset = []

        def dfs(l):
            if l == n:
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[l])
            dfs(l + 1)

            # skipping nums[i]
            subset.pop()
            dfs(l + 1)

        dfs(0)
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.subsets(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[1, 2, 3]],
    [[0]],
]
expected = [
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    [[], [0]],
]


sol = Solution()
sol.test(input, expected)
