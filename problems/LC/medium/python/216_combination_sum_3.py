"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice,
and the combinations may be returned in any order.


Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(curr, combo, total, cnt):
            if total == n and cnt == k:
                res.append(combo)
            if total > n or cnt == k:
                return

            for i in range(curr + 1, 10):
                if total + i <= n:
                    dfs(i, combo + [i], total + i, cnt + 1)

        dfs(0, [], 0, 0)
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.combinationSum3(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [3, 7],
    [3, 9],
    [4, 1],
    [9, 45],
]
expected = [
    [[1, 2, 4]],
    [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
    [],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9]],
]


sol = Solution()
sol.test(input, expected)
