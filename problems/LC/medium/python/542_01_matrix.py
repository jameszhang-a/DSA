"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:
Input:
mat =  [0,0,0],
       [0,1,0],
       [0,0,0]
Output:
       [0,0,0],
       [0,1,0],
       [0,0,0]

Example 2:
Input:
mat =  [0,0,0],
       [0,1,0],
       [1,1,1]
Output:
       [0,0,0],
       [0,1,0],
       [1,2,1]
"""

from collections import deque
from typing import List
from itertools import product


class Solution:
    def updateMatrix_dp(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        result = [[float("inf")] * m for _ in range(n)]

        # first path checks the min value between top and left positions
        for i, j in product(range(n), range(m)):
            if mat[i][j] == 0:
                result[i][j] = 0
            else:
                if i > 0:
                    result[i][j] = min(result[i][j], result[i - 1][j] + 1)
                if j > 0:
                    result[i][j] = min(result[i][j], result[i][j - 1] + 1)

        for i, j in product(reversed(range(n)), reversed(range(m))):
            if mat[i][j] == 0:
                continue
            else:
                if i < n - 1:
                    result[i][j] = min(result[i][j], result[i + 1][j] + 1)
                if j < m - 1:
                    result[i][j] = min(result[i][j], result[i][j + 1] + 1)

        return result

    def updateMatrix_bfs(self, mat: List[List[int]]) -> List[List[int]]:
        """
        find all 0's process each 1's around them
        bfs off of the 1's and update their distance
        """

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        n, m = len(mat), len(mat[0])
        q = deque([])

        # first round, add all the 0's to q
        # mark as unvisited with -1
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                new_i = i + di
                new_j = j + dj

                if (
                    new_i >= 0
                    and new_j >= 0
                    and new_i < n
                    and new_j < m
                    and mat[new_i][new_j] == -1
                ):
                    mat[new_i][new_j] = mat[i][j] + 1
                    q.append((new_i, new_j))
        return mat

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.updateMatrix_bfs(*input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [
        [
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
        ]
    ],
    [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]],
    [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]],
]
expected = [
    [
        [0, 1, 0, 1, 2],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
    ],
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
]


sol = Solution()

sol.test(input, expected)
