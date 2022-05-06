"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.



Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """too slow"""

        while 1:
            l, r = 0, 0
            modded = False

            while r < len(s):
                r += 1
                cnt = 1
                while r < len(s) and s[l] == s[r] and cnt < k:
                    cnt += 1
                    r += 1

                if cnt == k:
                    s = s[:l] + s[r:]
                    modded = True

                l += 1
                r = l

            if not modded:
                return s

        return "failed"

    def removeDuplicates_stack(self, s: str, k: int) -> str:
        stack = [1]  # use stack to store the cont of the current char
        i = 1
        while i < len(s):
            c = s[i]
            if c == s[i - 1]:
                if stack:
                    stack[-1] += 1
                else:
                    stack.append(1)
            else:
                stack.append(1)

            if stack[-1] == k:
                n = stack.pop()
                s = s[: i - n + 1] + s[i + 1 :]
                i = i - n + 1
                continue
            i += 1

        return s

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.removeDuplicates_stack(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["abcd", 2],
    ["deeedbbcccbdaa", 3],
    ["pbbcggttciiippooaais", 2],
]
expected = ["abcd", "aa", "ps", "wes"]


sol = Solution()
sol.test(input, expected)
