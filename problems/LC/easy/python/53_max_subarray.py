"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        two pointer
        """
        global_max, cur_max = nums[0], nums[0]

        for n in nums[1:]:
            if cur_max < 0:
                cur_max = n
            else:
                cur_max += n

            # or more concisely
            # cur_max = max(n, cur_max + n)
            global_max = max(global_max, cur_max)

        return global_max

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (ans := self.maxSubArray(*input)) != outputs[i]:
                print(f"{i} failed. Expected: {outputs[i]}, got: {ans}")
                continue

            print(f"{i} pass")


input = [[[-2, 1, -3, 4, -1, 2, 1, -5, 4]], [[1]], [[5, 4, -1, 7, 8]], [[1, 2]]]
expected = [6, 1, 23, 3]


sol = Solution()

sol.test(input, expected)
