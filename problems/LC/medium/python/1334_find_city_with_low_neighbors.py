"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents
a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most
distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.



Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.


Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.


Constraints:
2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""

import itertools
from typing import List
from collections import deque


class Solution:

    # dfs, Dijkstra's doesn't work because you could potentially go down a path that excludes some cities
    """
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # DFS
        # 1. visit all cities, keep count and total dist
        # 2. if dist > thresh
        #     move to next city origin

        # 3. return lowest city count


        # queue = []

        # pop next
        # add next to seen

        # for all neigh of next:
        #     if next dist < thresh:
        #         add to queue
        # track city count
        # next origin city


        matrix = {}

        for edge in edges:
            fro, to, weight = edge

            if fro not in matrix:
                matrix[fro] = []
            if to not in matrix:
                matrix[to] = []

            matrix[fro].append((to, weight))
            matrix[to].append((fro, weight))

        count = [0] * n
        for start in matrix.keys():
            q = deque([(start, 0)])
            seen = set()

            while q:
                curr, weight = q.popleft()
                seen.add(curr)

                if curr in matrix:
                    for to in matrix[curr]:
                        if to[0] not in seen and weight + to[1] <= distanceThreshold:
                            q.append((to[0], weight + to[1]))

            count[start] = len(seen)

        low = float("inf")
        res = ""
        for i in range(n - 1, -1, -1):
            if count[i] < low:
                low = count[i]
                res = i

        return res
    """

    INF = float("inf")
    # using floyd warshall algo to calculate path lengths for all cities combo
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # 1. find the min dist for all cities
        map = [[self.INF] * n for _ in range(n)]
        for i, j, w in edges:
            map[i][j] = w
            map[j][i] = w

        for k in range(n):
            for i, j in itertools.product(range(n), range(n)):
                if i == j:
                    map[i][i] = 0

                if i == k or j == k:
                    continue

                map[i][j] = min(map[i][j], map[i][k] + map[k][j])

        res = dict()
        for i, row in enumerate(map):
            count = 0
            for j, dist in enumerate(row):
                if dist <= distanceThreshold:
                    count += 1
            res[i] = count

        return min(reversed(res), key=lambda x: res[x])

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.findTheCity(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    [4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4],
    [5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2],
    [6, [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]], 417],
    [6, [[0, 1, 10], [0, 2, 1], [2, 3, 1], [1, 3, 1], [1, 4, 1], [4, 5, 10]], 20],
]
expected = [
    3,
    0,
    5,
    5,
]


sol = Solution()
sol.test(input, expected)
