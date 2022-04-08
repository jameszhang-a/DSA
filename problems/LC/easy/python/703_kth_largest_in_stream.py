"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""

from typing import List
import heapq


class KthLargest:

    """
    Keep a min heap and cap its size at k
    That way the kth element is just the root
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


k = 3
nums = [4, 5, 8, 2]  # 2, 4, 5, 8

obj = KthLargest(k, nums)
print(obj.add(3))  # 2, 3, 4, 5, 8
print(obj.add(5))  # 2, 3, 4, 5, 5, 8
print(obj.add(10))  # 2, 3, 4, 5, 5, 8, 10
print(obj.add(9))  # 2, 3, 4, 5, 5, 8, 9, 10
print(obj.add(4))  # 2, 3, 4, 4, 5, 5, 8, 9, 10
