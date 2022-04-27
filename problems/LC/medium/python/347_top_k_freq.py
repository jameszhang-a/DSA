"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.



Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

import heapq
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        O(n): count all elements
        O(nlogn): sort by count
        O(1): return top
        total: O(nlogn)
        """
        frequency = Counter(nums)
        keys = list(frequency.keys())
        keys.sort(key=frequency.get, reverse=True)
        return keys[:k]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        total: O(nlogk)
        """
        frequency = Counter(nums)
        keys = list(frequency.keys())
        res = heapq.nlargest(k, keys, key=frequency.get)
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.topKFrequent2(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [[1, 1, 1, 2, 2, 3], 2],
    [[1], 1],
]
expected = [
    [1, 2],
    [1],
]


sol = Solution()
sol.test(input, expected)
