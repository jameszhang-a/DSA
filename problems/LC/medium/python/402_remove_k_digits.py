"""
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output
must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing
which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []

        for c in num:
            while k and res and c < res[-1]:
                res.pop()
                k -= 1

            res.append(c)

        if k:
            res = res[:-k]

        return "".join(res).lstrip("0") or "0"

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.removeKdigits(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [["1432219", 3], ["10200", 1], ["1432219", 3], ["9", 1]]
expected = ["1219", "200", "1219", "0"]


sol = Solution()
sol.test(input, expected)
