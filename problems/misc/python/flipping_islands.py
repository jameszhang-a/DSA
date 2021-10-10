"""
Given a matrix of 1 and 0, turn all 1's that are not connect to the the edge
or any 1's that are connected to the edge into 0's

example:
[[0,0,1,0],
 [1,0,1,0],
 [0,1,0,0],
 [0,0,1,1]]
==>
[[0,0,1,0],
 [1,0,1,0],
 [0,0,0,0],
 [0,0,1,1]]

"""


def on_edge(i, j, i_len, j_len):
    return i == 0 or i == i_len - 1 or j == 0 or j == j_len - 1


def in_bounds(i, j, m):
    return i >= 0 and j >= 0 and i < len(m) and j < len(m[0])


def dfs(i, j, m, isOne):
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for x, y in moves:
        di, dj = i + x, j + y

        key = f"{di}{dj}"
        if in_bounds(di, dj, m) and m[di][dj] == 1 and key not in isOne:
            isOne[key] = True
            dfs(di, dj, m, isOne)


def island_flipping(m):
    isOne = {}

    for i, row in enumerate(m):
        for j, val in enumerate(row):
            print(f"{i},{j} : {val}")
            if val == 1 and on_edge(i, j, len(m), len(row)):
                isOne[f"{i}{j}"] = True
                dfs(i, j, m, isOne)

    for i, row in enumerate(m):
        for j, val in enumerate(row):
            if val == 1 and f"{i}{j}" not in isOne:
                m[i][j] = 0
    return m


matrix = [[0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
m2 = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

res = island_flipping(m2)

for row in res:
    print(row)
