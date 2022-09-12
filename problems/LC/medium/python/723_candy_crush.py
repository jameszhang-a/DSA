"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit
a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.



Example 1:
board = [
    [110, 5,   112, 113, 114],
    [210, 211, 5,   213, 214],
    [310, 311, 3,   313, 314],
    [410, 411, 412, 5,   414],
    [5,   1,   512, 3,   3],
    [610, 4,   1,   613, 614],
    [710, 1,   2,   713, 714],
    [810, 1,   2,   1,   1],
    [1,   1,   2,   2,   2],
    [4,   1,   4,   4,   1014],
]
Output = [
    [0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0],
    [0,   0,   0,   0,   0],
    [110, 0,   0,   0,   114],
    [210, 0,   0,   0,   214],
    [310, 0,   0,   113, 314],
    [410, 0,   0,   213, 414],
    [610, 211, 112, 313, 614],
    [710, 311, 412, 613, 714],
    [810, 411, 512, 713, 1014],
]

Example 2:
Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]


Constraints:

m == board.length
n == board[i].length
3 <= m, n <= 50
1 <= board[i][j] <= 2000
"""

from typing import List


class Solution:
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        check each horizontal for groups of 3, mark them as crushable
        check each vertical for groups of 3, mark them as crushable

        set all crushable to 0
        """

        m, n = len(board), len(board[0])
        done = False

        while True:
            crushable = set()
            done = True

            # check all horizontal crushable
            for i in range(m):
                for j in range(2, n):
                    if board[i][j] == board[i][j - 1] == board[i][j - 2] != 0:
                        crushable.update([(i, j), (i, j - 1), (i, j - 2)])
                        done = False

            # check all vertical crushable
            for i in range(2, m):
                for j in range(n):
                    if board[i][j] == board[i - 1][j] == board[i - 2][j] != 0:
                        crushable.update([(i, j), (i - 1, j), (i - 2, j)])
                        done = False

            # if above pass, then we done here
            if done:
                return board

            # time to crush
            for i, j in crushable:
                board[i][j] = 0

            # make candies fall
            for j in range(n):
                empty = 0

                # iterate from bottom up
                for i in range(m - 1, -1, -1):
                    offset = empty + i
                    if (i, j) in crushable:
                        empty += 1
                    else:
                        board[offset][j] = board[i][j]

                for i in range(empty):
                    board[i][j] = 0

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.candyCrush(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [
        [
            [110, 5, 112, 113, 114],
            [210, 211, 5, 213, 214],
            [310, 311, 3, 313, 314],
            [410, 411, 412, 5, 414],
            [5, 1, 512, 3, 3],
            [610, 4, 1, 613, 614],
            [710, 1, 2, 713, 714],
            [810, 1, 2, 1, 1],
            [1, 1, 2, 2, 2],
            [4, 1, 4, 4, 1014],
        ]
    ],
    [
        [
            [1, 3, 5, 5, 2],
            [3, 4, 3, 3, 1],
            [3, 2, 4, 5, 2],
            [2, 4, 4, 5, 5],
            [1, 4, 4, 1, 1],
        ]
    ],
]
expected = [
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [110, 0, 0, 0, 114],
        [210, 0, 0, 0, 214],
        [310, 0, 0, 113, 314],
        [410, 0, 0, 213, 414],
        [610, 211, 112, 313, 614],
        [710, 311, 412, 613, 714],
        [810, 411, 512, 713, 1014],
    ],
    [
        [1, 3, 0, 0, 0],
        [3, 4, 0, 5, 2],
        [3, 2, 0, 3, 1],
        [2, 4, 0, 5, 2],
        [1, 4, 3, 1, 1],
    ],
]


sol = Solution()
sol.test(input, expected)
