"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcazbcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest, l, r = 0, 0, 0

        while r < len(s):
            c = s[r]
            if c not in seen:
                seen.add(c)
                r += 1
                longest = max(longest, r - l)
            else:
                seen.remove(s[l])
                l += 1

        return longest

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.lengthOfLongestSubstring(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["abcabcbb"],
    ["bbbbb"],
]
expected = [
    3,
    1,
]


sol = Solution()
sol.test(input, expected)
