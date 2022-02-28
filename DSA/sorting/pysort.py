"""
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""
from typing import List


class pysort:
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Merge helper function that merges 2 lists in order"""
        merged, l, r = [], 0, 0

        while l < len(arr1) and r < len(arr2):
            if arr1[l] < arr2[r]:
                merged.append(arr1[l])
                l += 1
            else:
                merged.append(arr2[r])
                r += 1

        if l == len(arr1):
            merged.extend(arr2[r:])
        elif r == len(arr2):
            merged.extend(arr1[l:])

        return merged

    def merge_sort(self, nums: List[int]) -> List[int]:
        """Main recursion function, splits the array and calls merge on them"""
        n = len(nums)

        # base case
        if n == 1:
            return nums

        # split array into 2 halves
        mid = n // 2
        front = nums[:mid]
        back = nums[mid:]

        # recursion
        A = self.merge_sort(front)
        B = self.merge_sort(back)

        # merge at the end
        return self.merge(A, B)


sort = pysort()
nums = [5, 2, 3, 1, 8]

print(sort.merge_sort(nums))
