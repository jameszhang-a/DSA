"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        linear time, so no sorting
        """
        if not nums:
            return 0

        nums.sort()
        res, count = 1, 1
        for i, num in enumerate(nums[:-1]):
            if nums[i + 1] == num:
                """Skip duplicates"""
                res = max(res, count)
                continue

            if nums[i + 1] == num + 1:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.longestConsecutive(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[100, 4, 200, 1, 3, 2]],
    [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]],
    [[1, 3, 5, 7, 9]],
    [[1, 2, 0, 1]],
    [[0]],
    [[]],
    [[0, 0]],
]
expected = [
    4,
    9,
    1,
    3,
    1,
    0,
    1,
]


sol = Solution()
sol.test(input, expected)
