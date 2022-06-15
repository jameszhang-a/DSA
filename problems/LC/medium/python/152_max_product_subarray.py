"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


nums = [-4, -2, -5]
dp   = [-4, 8/-2, -40/10]
high = [-4, 8, 10]
low  = [1, -2, ]

ans = 10
"""
from typing import List


class Solution:
    # brute force, too slow
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]

        for i in range(len(nums)):
            cur_max = 1
            for j in range(i, len(nums)):
                cur_max *= nums[j]
                global_max = max(global_max, cur_max)

        return global_max

    def maxProductDP(self, nums):
        global_max, high, low = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            # need temp variable because the 'low' comparison needs original high value
            temp_high = max(nums[i], high * nums[i], low * nums[i])
            low = min(nums[i], low * nums[i], high * nums[i])

            high = temp_high

            global_max = max(global_max, high, low)

        return global_max

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.maxProductDP(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[2, 3, -2, 4]],
    [[-2, 0, -1]],
    [[-4, -2, -5]],
]
expected = [
    6,
    0,
    10,
]


sol = Solution()
sol.test(input, expected)
