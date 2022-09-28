"""
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously
push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the
dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling
or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        .L.R...LR..L..
        LL.RR.LLRRLL..

        nothing changes when two r/l are adjacent
        RR -> RR
        RL -> RL
        LR -> LR

        # Normal Case
        .R -> .R
        .L -> LL

        R. -> RR
        L. -> L.

        # Special Case
        R.L -> R.L

        .L.R...LR..L..

        two pointers, i j
        """

        def advance_middle(l, r):
            while l < r:
                dominoes[l] = "R"
                dominoes[r] = "L"
                l += 1
                r -= 1

        def set_R(l, r):
            for i in range(l, r):
                dominoes[i] = "R"

        # R keeps track of the last "R" location, -1 when not valid
        R, j = -1, 0
        dominoes = list(dominoes)

        for j in range(len(dominoes)):
            if dominoes[j] == "L":
                # when there hasn't been a valid "R"
                if R == -1:
                    # push all the L down for all the "."
                    i = j - 1
                    while i >= 0 and dominoes[i] == ".":
                        dominoes[i] = "L"
                        i -= 1
                # if there is a "R", advance both and meet in the middle
                # then set R as invalid again
                else:
                    # meet l and r in the middle
                    advance_middle(R + 1, j - 1)
                    R = -1

            elif dominoes[j] == "R":
                # if we see a "R", with a valid "R" in place already,
                # then we set everything in between to R
                if R != -1:
                    set_R(R, j)

                # update last used R
                R = j

        # in case the string ends in R...
        if R != -1:
            set_R(R, len(dominoes))

        return "".join(dominoes)

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.pushDominoes(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    ["RR.L"],
    [".L.R...LR..L.."],
    [".L.R.."],
    ["L.....RR.RL.....L.R."],
]
expected = [
    "RR.L",
    "LL.RR.LLRRLL..",
    "LL.RRR",
    "L.....RRRRLLLLLLL.RR",
]


sol = Solution()
sol.test(input, expected)
