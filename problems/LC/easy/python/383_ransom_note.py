"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count each letter frequency in ransome
        # count letter frequency in magazine
        # if ransome < frequency -> true

        a = Counter(ransomNote)
        b = Counter(magazine)
        b.subtract(a)

        for x in b.values():
            if x < 0:
                return False

        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        """
        Looks like it should be more efficient than the first way,
        but it's way slower for some reason
        """
        store = [0] * 26

        for c in magazine:
            store[ord(c) - ord("a")] += 1

        for c in ransomNote:
            store[ord(c) - ord("a")] -= 1
            if store[ord(c) - ord("a")] < 0:
                return False
        return True

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.canConstruct2(*input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    ["a", "b"],
    ["aa", "ab"],
    ["aa", "aab"],
]
expected = [False, False, True]


sol = Solution()

sol.test(input, expected)
