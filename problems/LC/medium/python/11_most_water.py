"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start on outer most walls, greedily shrink the side that creates the
        # most area
        def area(i, j):
            return (j - i) * min(height[i], height[j])

        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, area(l, r))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.maxArea(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[1, 8, 6, 2, 5, 4, 8, 3, 7]],
    [[1, 1]],
    [[1, 3, 5, 7, 9]],
    [[9, 7, 5, 3, 1]],
    [[1, 3, 2, 5, 25, 24, 5]],
]
expected = [49, 1, 10, 10, 24]


sol = Solution()
sol.test(input, expected)
