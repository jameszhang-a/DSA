"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        generate key for each anagram group:
            a:1, t:1, e:1  - ate, eat, tea
        sort to key: O(logn)
        iterate through list: O(n)
        """
        groups = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            groups[key].append(str)

        res = []
        for key in groups:
            res.append(groups[key])
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := sorted(self.groupAnagrams(*input))) != sorted(outputs[i]):
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [["eat", "tea", "tan", "ate", "nat", "bat"]],
    [[""]],
    [["a"]],
]
expected = [
    [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    [[""]],
    [["a"]],
]


sol = Solution()
sol.test(input, expected)
