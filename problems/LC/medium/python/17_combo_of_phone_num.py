"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that
1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        n = len(digits)
        res = []

        def dfs(i, curr):
            if i == n:
                res.append(curr)
                return

            num = digits[i]
            if num in mapping:
                for c in mapping[num]:
                    dfs(i + 1, curr + c)

        dfs(0, "")
        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.letterCombinations(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["23"],
    ["2"],
    [""],
]
expected = [
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
    ["a", "b", "c"],
    [],
]


sol = Solution()
sol.test(input, expected)
