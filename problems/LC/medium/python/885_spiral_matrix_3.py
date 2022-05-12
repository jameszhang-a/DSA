"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid,
and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue
our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.



Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],
         [0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
"""
from typing import List


class Solution:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
        """
        walk in sequence: 1, 1, 2, 2, 3, 3, ...
        formula for seq : n // 2 + 1
        """
        steps = [[r, c]]
        n = 0
        dir = 0
        while len(steps) < (rows * cols):
            moves = n // 2 + 1
            for _ in range(moves):
                r += self.directions[dir % 4][0]
                c += self.directions[dir % 4][1]

                if 0 <= r < rows and 0 <= c < cols:
                    steps.append([r, c])

            n += 1
            dir += 1

        return steps

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.spiralMatrixIII(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [5, 6, 1, 4],
    [1, 4, 0, 0],
]
expected = [
    [
        [1, 4],
        [1, 5],
        [2, 5],
        [2, 4],
        [2, 3],
        [1, 3],
        [0, 3],
        [0, 4],
        [0, 5],
        [3, 5],
        [3, 4],
        [3, 3],
        [3, 2],
        [2, 2],
        [1, 2],
        [0, 2],
        [4, 5],
        [4, 4],
        [4, 3],
        [4, 2],
        [4, 1],
        [3, 1],
        [2, 1],
        [1, 1],
        [0, 1],
        [4, 0],
        [3, 0],
        [2, 0],
        [1, 0],
        [0, 0],
    ],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
]


sol = Solution()
sol.test(input, expected)
