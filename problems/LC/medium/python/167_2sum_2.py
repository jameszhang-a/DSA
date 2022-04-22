"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same
element twice.

Your solution must use only constant extra space.


Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since it's constant space, can't store the position of each element
        # for each num, binary search for the difference
        # O(NlogN)

        for i, n in enumerate(numbers[:-1]):
            diff = target - n

            # now search for partner
            # don't have to search backwards just because of staying ahead

            l, r = i + 1, len(numbers) - 1

            while l <= r:
                m = (l + r) // 2
                if diff == numbers[m]:
                    return [i + 1, m + 1]

                elif numbers[m] < diff:
                    l = m + 1
                else:
                    r = m - 1

        return [0, 0]

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.twoSum(*input) != outputs[i]:
                print(self.twoSum(*input))
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [[5, 25, 75], 100],
    [[2, 7, 11, 15], 9],
    [[2, 3, 4], 6],
    [[-1, 0], -1],
]
expected = [
    [2, 3],
    [1, 2],
    [1, 3],
    [1, 2],
]


sol = Solution()

sol.test(input, expected)
