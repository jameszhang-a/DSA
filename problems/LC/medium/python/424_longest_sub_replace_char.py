"""
You are given a string s and an integer k. You can choose any character
of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""


import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = collections.Counter()
        res, n, maxf = 0, len(s), 0

        l = 0
        for r in range(n):
            store[s[r]] += 1
            maxf = max(store[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                store[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.characterReplacement(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["AABABBA", 1],
    ["ABAB", 2],
]
expected = [
    4,
    4,
]


sol = Solution()
sol.test(input, expected)
