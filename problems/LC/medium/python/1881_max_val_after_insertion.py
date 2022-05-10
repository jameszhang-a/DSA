"""
You are given a very large integer n, represented as a string, and an integer digit x.
The digits in n and the digit x are in the inclusive range [1, 9], and n may represent a negative number.

You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n
You cannot insert x to the left of the negative sign.

For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
Return a string representing the maximum value of n after the insertion.



Example 1:
Input: n = "99", x = 9
Output: "999"
Explanation: The result is the same regardless of where you insert 9.

Example 2:
Input: n = "-13", x = 2
Output: "-123"
Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.
"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0].isalnum():
            for i, c in enumerate(n):
                if x > int(c):
                    return n[:i] + str(x) + n[i:]
            return f"{n}{x}"
        else:
            for i, c in enumerate(n[1:]):
                if x < int(c):
                    return n[: i + 1] + str(x) + n[i + 1 :]
            return f"{n}{x}"

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.maxValue(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["-13", 2],
    ["-134", 9],
    ["-234", 1],
    ["99", 9],
    ["429", 3],
    ["429", 9],
    ["429", 1],
    ["-132", 3],
]
expected = [
    "-123",
    "-1349",
    "-1234",
    "999",
    "4329",
    "9429",
    "4291",
    "-1323",
]


sol = Solution()
sol.test(input, expected)
