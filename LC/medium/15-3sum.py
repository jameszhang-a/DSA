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
    def bSearch(self, nums, tar):
        l = 0
        h = len(nums)-1
        m = (h + l) // 2
        
        
        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        # * Brute force, O(n^3)
        # for x in range(len(nums)):
        #     for y in range(x+1, len(nums)):
        #         for k in range(y+1, len(nums)):
        #             if (nums[x] + nums[y] + nums[k] == 0):
        #                 ans.append([nums[x], nums[y], nums[k]])

        # * Binary search
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[j+1:]
                if third := self.bSearch(sorted(temp), -(nums[i] + nums[j])):
                    print("Hello")
                else:
                    print("No")

        return ans


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
