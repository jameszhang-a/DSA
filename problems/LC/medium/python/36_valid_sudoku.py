"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
from itertools import product
from typing import List


class Solution:
    directions = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Checklist:
        - each row: i
        - each col: j
        - each box: 1, 4, 7
        """

        flipped = [[0] * 9 for _ in range(9)]

        # checking each row
        for i in range(9):
            row = []
            for j in range(9):
                letter = board[i][j]
                if letter.isalnum():
                    row.append(letter)

                flipped[j][i] = letter  # saving a transposed matrix for the columns

            if len(row) != len(set(row)):
                return False

        # checking row of transposed matrix, i.e. each column
        for i in range(9):
            row = []
            for j in range(9):
                letter = flipped[i][j]
                if letter.isalnum():
                    row.append(letter)

            if len(row) != len(set(row)):
                return False

        for i, j in product(range(9), range(9)):
            # product produces all i,j pairs. i.e. loops through each cell
            box = []
            if i % 3 == 1 and j % 3 == 1:
                for di, dj in self.directions:
                    letter = board[di + i][dj + j]
                    if letter.isalnum():
                        box.append(letter)

            if len(box) != len(set(box)):
                return False

        return True

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.isValidSudoku(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print()
                continue

            print(f"{i} pass")
            print()


input = [
    [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    ],
    [
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    ],
    [
        [
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    ],
    [
        [
            ["9", ".", ".", "6", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "6", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "1", ".", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "8"],
            [".", ".", ".", ".", ".", "8", ".", ".", "."],
            [".", ".", ".", "4", ".", ".", "2", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "1"],
            ["6", ".", ".", ".", "1", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    ],
]
expected = [
    True,
    False,
    False,
    False,
]


sol = Solution()
sol.test(input, expected)
