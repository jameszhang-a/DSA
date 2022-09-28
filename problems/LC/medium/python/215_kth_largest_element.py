"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.



Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        use heap

        - min heap
            keep size to k
            if new element is greater than top element
            pop top and add new element

        return heap
        """

        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.findKthLargest(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[3, 2, 1, 5, 6, 4], 2],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
]
expected = [
    5,
    4,
]


sol = Solution()
sol.test(input, expected)
