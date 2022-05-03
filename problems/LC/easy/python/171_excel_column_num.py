"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i, c in enumerate(columnTitle[::-1]):
            val = ord(c) - ord("A") + 1
            total += val * 26 ** (i)

        return total

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.titleToNumber(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["A"],
    ["AB"],
    ["ZY"],
]
expected = [
    1,
    28,
    701,
]


sol = Solution()
sol.test(input, expected)
