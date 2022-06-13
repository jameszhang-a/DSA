"""
You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums.
If n == 1,
    end the process.
Otherwise,
    create a new 0-indexed integer array newNums of length n / 2.

For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).

Replace the array nums with newNums.
Repeat the entire process starting from step 1.

Return the last number that remains in nums after applying the algorithm.



Example 1:
Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.


Example 2:
Input: nums = [3]
Output: 3
Explanation: 3 is already the last remaining number, so we return 3.
"""
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:

        # m = 0 when even index (min value)
        # m = 1 when odd index (max value)
        def recur(nums, m):
            n = len(nums)

            if n == 1:
                return nums[0]

            return (
                max(recur(nums[: n // 2], 0), recur(nums[n // 2 :], 1))
                if m
                else min(recur(nums[: n // 2], 0), recur(nums[n // 2 :], 1))
            )

        return recur(nums, 0)

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.minMaxGame(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[1, 3, 5, 2, 4, 8, 2, 2]],
    [[3]],
    [[999, 939, 892, 175, 114, 464, 850, 107]],
]
expected = [
    1,
    3,
    850,
]


sol = Solution()
sol.test(input, expected)
