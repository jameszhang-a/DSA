"""
Given matrix, an n x n square matrix of integers, let's define its a -border as the union of
Its leftmost and rightmost columns, as well as its top and bottom rows.

If we were to remove the matrix's o -border, then the o-border of the resulting matrix can be
defined as the 1 -border of the original matrix. We can continue this way to define the 2
border. 3-border, etc.

Example
before =[[9, 7, 4, 5],
         [1, 6, 2, -6],
         [12, 20, 2, 0],
         [-5, -6, 7, -2]]

after  =[[-6, -6, -5, -2],
         [12, 2, 2, 0],
         [9, 20, 6, 1],
         [7, 7, 5, 4]]

"""
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(matrix):
    n = len(matrix)

    if n == 1:
        return []

    res = [[None] * n for _ in range(n)]
    k = n // 2

    for i in range(k):
        A = [matrix[i][i]]
        col = row = i
        for direction in directions:
            while True:
                nextRow = row + direction[0]
                nextCol = col + direction[1]

                if not (i <= nextRow < n - i and i <= nextCol < n - i):
                    break

                row, col = nextRow, nextCol
                A.append(matrix[nextRow][nextCol])

        border = sorted(A[:-1])[::-1]
        res[i][i] = border.pop()

        for direction in directions:
            while True:
                nextRow = row + direction[0]
                nextCol = col + direction[1]

                if not (i <= nextRow < n - i and i <= nextCol < n - i) or nextCol == i == nextRow:
                    break

                row, col = nextRow, nextCol
                res[nextRow][nextCol] = border.pop()
    return res


m = [[9, 7, 4, 5], [1, 6, 2, -6], [12, 20, 2, 0], [-5, -6, 7, -2]]
res = solution(m)

print("\n".join(["".join(["{:4}".format(item if item else 0) for item in row]) for row in res]))


m = [[101]]
res = solution(m)

print("\n".join(["".join(["{:4}".format(item if item else 0) for item in row]) for row in res]))


m = [[12, 5], [4, 3]]
res = solution(m)

print("\n".join(["".join(["{:4}".format(item if item else 0) for item in row]) for row in res]))
