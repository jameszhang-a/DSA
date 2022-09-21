"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1Write an algorithm to determine if a number n is happy.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def process(n):
            return sum([int(d) ** 2 for d in str(n)])

        seen = set()
        while True:
            n = process(n)
            if n not in seen:
                seen.add(n)
            else:
                return False

            if n == 1:
                return True

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.isHappy(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [19],
    [2],
    [1],
]
expected = [True, False, True]


sol = Solution()
sol.test(input, expected)
