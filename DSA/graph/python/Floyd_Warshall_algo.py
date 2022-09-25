"""
Similar to Dijkstra's algo in that it finds shortest path

This returns ALL shortest paths from each node to another in a weighted graph

Works for directed or undirected

Does NOT work for negative cycles, i.e. negative edge weights

Time:  O(n^3)
space: O(n^2)
"""
from itertools import product


INF = float("inf")

# input graph:
#   each value is dist from i to j
#   INF in the beginning means there's no path
G = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0],
]


def floyd_warshall(graph):
    """
    Loops n times:
        each loop traverse whole graph: n x n
    """
    N = len(graph)

    for k in range(N):
        # for each iteration mod the matrix and update the values of each destination as:
        # min( current path, start to k + k to end ), where k is each iteration
        for i, j in product(range(N), range(N)):
            if i == k or j == k:
                continue

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


print(floyd_warshall(G))
"""
expect:
    [0, 3, 7, 5],
    [2, 0, 6, 4],
    [3, 1, 0, 5],
    [5, 3, 2, 0],
"""
