"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves
right by one position.

Return the max sliding window.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque([])
        res = []
        for i in range(len(nums)):
            # can't use the max anymore bc it's out of the window
            if q and i - q[0] >= k:
                q.popleft()

            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

            if i > k - 2:
                res.append(nums[q[0]])

        return list(res)

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.maxSlidingWindow(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [[[1, 3, -1, -3, 5, 3, 6, 7], 3], [[1], 1], [[1, -1], 1], [[7, 2, 4], 2]]
expected = [[3, 3, 5, 5, 6, 7], [1], [1, -1], [7, 4]]


sol = Solution()
sol.test(input, expected)
