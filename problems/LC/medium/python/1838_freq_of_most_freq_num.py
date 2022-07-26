"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation,
you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most
k operations.



Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element
two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        The array needs to be in increasing order.

        we can keep adding to the bucket if: k + sum >= length * largest
        for example, k = 5:
            window: 1, 2, 4
            k + sum = 5 + 7 = 12
            length * largest = 12

            it's >= therefore it's valid
        """
        freq, l, s = 0, 0, 0
        n = len(nums)
        nums.sort()

        for r in range(n):
            s += nums[r]

            # keep moving the left pointer up, removing another from the sum
            while (k + s) < ((r - l + 1) * nums[r]):
                s -= nums[l]
                l += 1

            freq = max(freq, r - l + 1)

        return freq

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.maxFrequency(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[1, 2, 4], 5],
    [[1, 4, 8, 13], 5],
    [[3, 9, 6], 2],
]
expected = [
    3,
    2,
    1,
]


sol = Solution()
sol.test(input, expected)
