"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.



Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        - sort both strings and check 1 by 1 (n log(n))
        - count num letters in both (n)
        """
        count_s = [0] * 26
        count_t = [0] * 26

        for c in s:
            count_s[ord(c) - ord("a")] += 1

        for c in t:
            count_t[ord(c) - ord("a")] += 1

        return count_s == count_t

    def isAnagram_2(self, s: str, t: str) -> bool:
        # faster
        if len(s) != len(t):
            return False

        for c in set(s):
            if s.count(c) != t.count(c):
                return False

        return True

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.isAnagram_2(input[0], input[1]) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    ["anagram", "nagaram"],
    ["rat", "car"],
]
expected = [
    True,
    False,
]


sol = Solution()
nums = [3, 2, 4]
target = 6
s = "A man, a plan, a canal: Panama"

sol.test(input, expected)
