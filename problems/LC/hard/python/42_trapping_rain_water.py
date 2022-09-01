"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.



Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6
units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

9, 5, 4, 3, 8, 6, 5, 4, 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List


class Solution:
    # Slow algo, need to check for maxRight every iteration

    # def trap(self, height: List[int]) -> int:
    #     """
    #     at each position, the max amount of water is:
    #         # this forms the walls without spilling
    #         min(max height to the left, max hight to the right) - curr height
    #     """
    #     n = len(height)
    #     if n < 3:
    #         return 0

    #     l, i = 0, 1
    #     res = 0
    #     while i < (n - 1):
    #         L = height[l]
    #         curr = height[i]

    #         if curr >= L:
    #             l = i
    #             i += 1
    #             continue

    #         R = max(height[i + 1 :])

    #         res += min(L, R) - curr if min(L, R) - curr > 0 else 0
    #         i += 1

    #     return res

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]

        res = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]

        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.trap(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]],
    [[4, 2, 0, 3, 2, 5]],
]
expected = [
    6,
    9,
]


sol = Solution()
sol.test(input, expected)
