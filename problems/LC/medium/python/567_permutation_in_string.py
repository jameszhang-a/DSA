"""
Given two strings s1 and s2, return true if s2 contains a permutation
of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring
of s2.



Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = Counter(s1)
        countS2 = Counter(s2[: len(s1)])
        if not countS1 - countS2:
            return True

        for i in range(len(s2) - len(s1)):
            countS2[s2[i]] -= 1
            countS2[s2[i + len(s1)]] += 1
            if not countS1 - countS2:
                return True

        return False

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.checkInclusion(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [["ab", "eidbaooo"], ["ab", "eidboaoo"], ["adc", "dcda"]]
expected = [True, False, True]


sol = Solution()
sol.test(input, expected)
