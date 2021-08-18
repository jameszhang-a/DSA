# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.


# Example 1:

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
# Example 2:

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]
# Explanation: [4, 9] is also accepted.


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
import numpy as np

x = np.array([(1, 2), (3, 4)], dtype=[('a', '<i4'), ('b', '<i4')])
x['a']

class Solution:
    def intersection(self, nums1, nums2):

        ############ BINARY SEARCH BAD ##################
        #     cur = set()
        #     for num in nums1:
        #         if self.bSearch(sorted(nums2), num):
        #             cur.add(num)

        #     return cur

        # def bSearch(self, arr, tar):
        #     l = 0
        #     h = len(arr)-1

        #     while l <= h:
        #         m = (l+h)//2
        #         if tar < arr[m]:
        #             h = m-1
        #         elif tar > arr[m]:
        #             l = m+1
        #         else:
        #             return 1
        #     return 0

        ############ SIMPLE SETS ######################
        return set(nums1)&set(nums2)


sol = Solution()
x = sol.intersection([1, 2, 2, 1,6,5],
                     [2, 2,3,5,6,8])
print(x)
