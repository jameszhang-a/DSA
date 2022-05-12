"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            # this prevents int overflow error if left and right are large enough
            mid = (l + r) >> 1
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return l if nums[l] == target else -1

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.search(input[0], input[1]) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [[-1, 0, 3, 5, 9, 12], 13],
    [[-1, 0, 3, 5, 9, 12], 9],
    [[-1, 0, 3, 5, 9, 12], 2],
    [[5], 5],
]
expected = [
    -1,
    4,
    -1,
    0,
]


sol = Solution()
nums = [3, 2, 4]
target = 6
s = "A man, a plan, a canal: Panama"

sol.test(input, expected)
