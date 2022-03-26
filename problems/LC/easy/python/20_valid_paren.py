"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c not in key:
                stack.append(c)
            else:
                if stack and key[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack


sol = Solution()
nums = [3, 2, 4]
target = 6
s = "(])"

print(sol.isValid(s))
