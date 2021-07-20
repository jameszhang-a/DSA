from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = nums[0]
        second_max = float('-inf')
        third_max = float('-inf')

        if len(nums) < 3:
            return max(nums)

        for num in nums:
            if num == first_max or num == second_max or num == second_max:
                continue
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num

        return third_max if third_max != float('-inf') else first_max


test = Solution()
print(test.thirdMax([-51, 2]))
