"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character
may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        example input: s = aaa, t = bbb, return True
        s = aaa, t = abc, return False
        s = aaa, t = bb, return False

        aaa
         ^
        abc

        """

        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        swaps = {}
        mapped = set()
        for i, c in enumerate(s):
            if c not in swaps:
                if t[i] in mapped:
                    return False

                swaps[c] = t[i]
                mapped.add(t[i])
                continue

            if swaps[c] != t[i]:
                return False

        return True

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.isIsomorphic(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [["egg", "add"], ["foo", "bar"], ["paper", "title"], ["badc", "baba"]]
expected = [True, False, True, False]


sol = Solution()
sol.test(input, expected)
