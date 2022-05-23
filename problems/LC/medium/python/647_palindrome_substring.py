"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.


Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        if there is a palindrome, we can expand off of both sides and check if new string is palindrome
        """

        def build(l, r):
            ct = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ct += 1
                    l -= 1
                    r += 1
                else:
                    break
            return ct

        count = 0
        for i, x in enumerate(s):
            # first count palindromes if middle is odd
            count += build(i, i)
            # count palindrome if middle is even
            count += build(i, i + 1)
        return count

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.countSubstrings(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [["abc"], ["aaa"], ["fdsklf"]]
expected = [3, 6, 6]


sol = Solution()
sol.test(input, expected)
