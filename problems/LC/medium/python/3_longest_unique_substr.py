"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
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
        charSet = set()
        l, r, res = 0, 0, 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                charSet.remove(s[l])
                l += 1

        return res


sol = Solution()
s = "abcabcbb"

print(sol.lengthOfLongestSubstring(s))
