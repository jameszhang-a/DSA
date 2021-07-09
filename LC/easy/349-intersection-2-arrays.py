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

class Solution:
    def intersection(self, nums1, nums2):
        cur = set()
        for num in nums1:
            if self.bSearch(sorted(nums2), num):
                cur.add(num)

        return cur

    def bSearch(self, arr, tar):
        l = 0
        h = len(arr)-1

        # edge case
        if arr[l] == tar or arr[h] == tar:
            return 1

        while l < h:
            m = (l+h)//2
            if tar == arr[l] or tar == arr[h]:
                return 1
            elif tar < arr[m]:
                h = m-1
            elif tar > arr[m]:
                l = m+1
            else:
                return 1
        return 0


sol = Solution()
x = sol.intersection([1], [1])
print(x)
