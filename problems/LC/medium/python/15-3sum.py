# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
# i != j,
# i != k,
# j != k,
# nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []


# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        iterate through list with left pointer
        use middle and right pointer to find if there's a complement
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 1):
            # skips duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            curr = nums[i]
            m, r = i + 1, len(nums) - 1

            while m < r:
                sum = nums[m] + nums[r] + curr

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    m += 1
                else:
                    ans.append([curr, nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
        return ans

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.threeSum(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[-1, 0, 1, 2, -1, -4]],
    [[0, 0, 0, 0, 0]],
    [[0]],
    [[-2, 0, 1, 1, 2]],
]
expected = [
    [[-1, -1, 2], [-1, 0, 1]],
    [[0, 0, 0]],
    [],
    [[-2, 0, 2], [-2, 1, 1]],
]


sol = Solution()
sol.test(input, expected)
