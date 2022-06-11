"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        stuff
        org: [1, 2, 3, 4]
        L:   [1, 1, 2, 6]
        R:   [24,12,4, 1]
        """
        n = len(nums)

        L, R = [1] + ((n - 1) * [0]), ((n - 1) * [0]) + [1]

        for i in range(1, n):
            L[i] = L[i - 1] * nums[i - 1]
            R[n - 1 - i] = R[n - i] * nums[n - i]

        return [L[i] * R[i] for i in range(n)]

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.productExceptSelf(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[1, 2, 3, 4]],
    [[-1, 1, 0, -3, 3]],
]
expected = [
    [24, 12, 8, 6],
    [0, 0, 9, 0, 0],
]


sol = Solution()
sol.test(input, expected)
