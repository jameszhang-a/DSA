"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < len(s) - 1:
                l += 1
            while not s[r].isalnum() and r >= 0:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.isPalindrome(input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    ".,",
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
]
expected = [
    True,
    True,
    False,
    True,
]


sol = Solution()
nums = [3, 2, 4]
target = 6
s = "A man, a plan, a canal: Panama"

sol.test(input, expected)
print(sol.isPalindrome("race a car"))
