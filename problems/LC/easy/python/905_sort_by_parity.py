"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """simple nlog(n) solution"""
        return sorted(nums, key=lambda x: x % 2)

    def sortArrayByParity_2(self, nums):
        """O(n) quicksort"""
        i, j = 0, len(nums) - 1

        # loop invairant: everything below i is even, everything above j is 1
        while i < j:
            # case: if i is odd and j is even
            if nums[i] % 2 and (nums[j] + 1) % 2:
                nums[i], nums[j] = nums[j], nums[i]

            # if i is even, increment
            if (nums[i] + 1) % 2:
                i += 1
            # if j is odd, decrement
            if (nums[j]) % 2:
                j -= 1

        return nums

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.sortArrayByParity_2(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[3, 1, 2, 4]],
    [[0]],
]
expected = [
    [2, 4, 3, 1],
    [0],
]


sol = Solution()
sol.test(input, expected)
