"""
According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state:
live (represented by a 1) or dead (represented by a 0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken
from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the
current state, where births and deaths occur simultaneously. Given the current state of the
m x n grid board, return the next state.



Example 1:
Input: board = [[0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]]

Output: board =[[0,0,0],
                [1,0,1],
                [0,1,1],
                [0,1,0]]


Example 2:
Input: [[1,1],
        [1,0]]

Output:[[1,1],
        [1,1]]
"""


from typing import List


class Solution:
    directions = {
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    }

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        in place solution:
        live -> dead = -1
        dead -> live = 2
        live -> live = 1
        dead -> dead = 0
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                num_neighbors = self.neighbors(board, i, j)

                if curr:
                    """if alive"""
                    if num_neighbors == 2 or num_neighbors == 3:
                        continue
                    else:
                        board[i][j] = -1

                else:
                    """if dead"""
                    if num_neighbors == 3:
                        board[i][j] = 2

        for i, row in enumerate(board):
            for j in range(len(row)):
                if row[j] == -1:
                    row[j] = 0
                if row[j] == 2:
                    row[j] = 1

        return board

    def neighbors(self, graph, i, j):
        num = 0
        for di, dj in self.directions:
            new_i, new_j = i + di, j + dj

            # edge detection, can't go over bounds
            if new_i < 0 or new_j < 0 or new_i >= len(graph) or new_j >= len(graph[0]):
                continue

            if abs(graph[new_i][new_j]) == 1:
                num += 1

        return num

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.gameOfLife(*input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]],
    [[[1, 1], [1, 0]]],
]
expected = [
    [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
    [[1, 1], [1, 1]],
]


sol = Solution()

sol.test(input, expected)
