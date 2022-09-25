"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings,
and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B,
with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are
primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.



Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Constraints:
1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        1. identify primitives
        2. remove outer paren
        3. join
        """

        stack = []
        res = []

        for c in s:
            if not stack:
                stack.append("(")
                continue

            if stack[-1] == "(" and c == ")":
                stack.pop()
                if stack:
                    res.append(")")

            else:
                stack.append(c)
                res.append(c)

        return "".join(res)

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.removeOuterParentheses(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [["(()())(())"], ["(()())(())(()(()))"], ["()()"]]
expected = ["()()()", "()()()()(())", ""]


sol = Solution()
sol.test(input, expected)
