"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of
s such that every character in t (including duplicates) is included in the window. If there is no
such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # counter of the substring that we are looking for
        want_count = Counter(t)

        # two pointers
        left, right = 0, 0

        # flag for checking if the program has found ANY valid substrings
        found_sub = False

        # number of chars we have to find
        counter = len(t)

        # final result
        res = float("inf"), 0, 0

        #
        while right < len(s):

            # check if the current char we are on is a part of the substring we want
            # if yes, we decrease the # of chars we are still looking for
            if want_count[s[right]] > 0:
                counter -= 1

            # looking for one less chars (e.g. before: {'b':2}, new: {'b':1})
            want_count[s[right]] -= 1
            right += 1

            # * while the window is stable
            # i.e. number of chars we are looking for is 0
            # we shrink the window from the left
            while counter == 0:
                found_sub = True  # mark that we found at least one valid subs

                # check that the current substring is the shortest
                if (right - left) < res[0]:
                    res = right - left, left, right

                # indicate that we left out a char in the window
                want_count[s[left]] += 1

                # if the char we left out is from the original substring that we want,
                #   add to counter, indicating window is no longer valid
                if want_count[s[left]] > 0:
                    counter += 1

                left += 1

        return s[res[1] : res[2]] if found_sub else ""

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.minWindow(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["ADOBECODEBANC", "ABC"],
    ["a", "a"],
    ["a", "aa"],
    ["ab", "a"],
]
expected = [
    "BANC",
    "a",
    "",
    "a",
]


sol = Solution()
sol.test(input, expected)
