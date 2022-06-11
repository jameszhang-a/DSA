"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time:   O(N)
        Space:  O(N)
        """
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.containsDuplicate(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [[[1, 2, 3, 1]], [[1, 2, 3, 4]], [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]]
expected = [True, False, True]


sol = Solution()
sol.test(input, expected)
