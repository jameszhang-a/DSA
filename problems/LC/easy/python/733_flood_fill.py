"""
An image is represented by an m x n integer grid image where
image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of the
same color as the starting pixel, plus any pixels connected 4-directionally to
those pixels (also with the same color), and so on. Replace the color of all of
the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels)
are colored with the new color.

Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
"""

from tkinter import image_names
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        I = len(image)
        J = len(image[0])

        if (old := image[sr][sc]) == newColor:
            # no need to change anything
            return image

        def recur(i, j):
            if image[i][j] == old:
                image[i][j] = newColor

                if i - 1 >= 0:
                    recur(i - 1, j)
                if i + 1 < I:
                    recur(i + 1, j)
                if j - 1 >= 0:
                    recur(i, j - 1)
                if j + 1 < J:
                    recur(i, j + 1)

        recur(sr, sc)

        return image

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if self.floodFill(*input) != outputs[i]:
                print(f"{i} failed")
                continue

            print(f"{i} pass")


input = [
    [[[0, 0, 0], [0, 1, 1]], 1, 1, 1],
    [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2],
    [[[0, 0, 0], [0, 0, 0]], 0, 0, 2],
]
expected = [
    [[0, 0, 0], [0, 1, 1]],
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
    [[2, 2, 2], [2, 2, 2]],
]


sol = Solution()
sol.test(input, expected)
